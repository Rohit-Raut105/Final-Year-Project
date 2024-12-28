from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10, verbose_name="Enter your phone number", null=False, blank=False)
    address = models.CharField(max_length=50, verbose_name="Enter your address", null=False, blank=False)
    def __str__(self):
        return f"{self.user.username}'s Profile"
