from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    deposit = models.FloatField(default=0)
    # REQUIRED_FIELDS = ["username"]


class Role(models.Model):
    class RoleNames(models.TextChoices):
        BUYER = 'Buyer'
        SELLER = 'Seller'
    name = models.CharField(max_length=100, choices=RoleNames)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


