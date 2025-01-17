from django.contrib.auth.models import AbstractUser
from django.db import models

class UserProfile(AbstractUser):
    total_expenses = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_saving = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    profile_picture = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics')

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='userprofile_set',  
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='userprofile_set', 
        blank=True
    )

    def __str__(self):
        return self.username
