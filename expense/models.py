from django.db import models
from django.conf import settings
from datetime import date

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Expense(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default=None, blank=False, null=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    date = models.DateField(default=date.today)

    def __str__(self):
        return f"{self.name} - {self.category.name if self.category else 'Miscellaneous'} - {self.amount} on {self.date}"

    def save(self, *args, **kwargs):
        if not self.category:
            self.category, created = Category.objects.get_or_create(name='Miscellaneous')
        super().save(*args, **kwargs)
