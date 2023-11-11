from django.db import models
from user.models import User


# Create your models here.


class Account(models.Model):
    class Status(models.IntegerChoices):
        ACCEPT = 1
        REJECT = 2

    user = models.ForeignKey(User, db_index=True, on_delete=models.RESTRICT)
    bank = models.CharField(max_length=20)
    sheba_number = models.CharField(max_length=24, unique=True)
    card_number = models.CharField(max_length=24, unique=True)
    status = models.PositiveSmallIntegerField(db_index=True, choices=Status.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




class CompanyAccount(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    bank_name = models.CharField(max_length=30)
    sheba_number = models.CharField(max_length=24, unique=True)
    account_number = models.CharField(max_length=24, unique=True)
    amount_limit = models.DecimalField(default=0, max_digits=32, decimal_places=20)
    daily_amount_limit = models.DecimalField(default=0, max_digits=32, decimal_places=20)
    company_daily_amount_limit = models.DecimalField(default=0, max_digits=32, decimal_places=20)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
