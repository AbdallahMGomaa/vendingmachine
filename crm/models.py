from django.contrib.auth.models import AbstractUser
from django.db import models
from authentication.models import User


# Create your models here.


class Product(models.Model):
    amount_available = models.IntegerField(default=0)
    cost = models.IntegerField()
    name = models.CharField(max_length=100)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)


class Transaction(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
