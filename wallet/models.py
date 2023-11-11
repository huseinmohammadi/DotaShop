from django.core.validators import MinValueValidator
from django.db import models

from bank_account.models import Account, CompanyAccount
from user.models import User


# Create your models here.


class Wallet(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.RESTRICT
    )
    balance = models.DecimalField(default=0, max_digits=20, decimal_places=8, validators=[MinValueValidator(0)])
    balance_locked = models.DecimalField(default=0, max_digits=20, decimal_places=8, validators=[MinValueValidator(0)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class WalletTransaction(models.Model):
    wallet = models.ForeignKey(
        Wallet,
        on_delete=models.RESTRICT,
    )
    old_balance = models.DecimalField(default=0, max_digits=20, decimal_places=8)
    new_balance = models.DecimalField(default=0, max_digits=20, decimal_places=8)
    desc = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class DepositRegistration(models.Model):
    class Status(models.TextChoices):
        SUCCEEDED = "SUCCEEDED"
        FAILED = "FAILED"
        REQUESTED = "REQUESTED"

    amount = models.DecimalField(default=0, max_digits=32, decimal_places=20)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    origin_account = models.ForeignKey(Account, on_delete=models.CASCADE)
    destination_account = models.ForeignKey(CompanyAccount, on_delete=models.CASCADE)
    deposit_id = models.CharField(max_length=255, null=True, blank=True)
    tracking_code = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    deposit_date = models.DateTimeField(null=True, blank=True)
    bank_receipt = models.CharField(max_length=500, null=True, blank=True)
    status = models.CharField(choices=Status.choices, db_index=True, max_length=255, default='REQUESTED')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
