from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.conf import settings


class SavingGoal(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    name = models.CharField(max_length=255, blank=True)
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    amount_saved = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    target_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    creation_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.amount_saved}/{self.target_amount}"

    def save(self, *args, **kwargs):
        if not self.name:
            goal_count = SavingGoal.objects.filter(user=self.user).count()
            self.name = f"Goal {goal_count + 1}"
        super().save(*args, **kwargs)

    def progress(self):
        return (self.amount_saved / self.target_amount) * 100
