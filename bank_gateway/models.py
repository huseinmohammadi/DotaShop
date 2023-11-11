from django.core.validators import MinValueValidator
from django.db import models

from user.models import User


# Create your models here.


class BankGateway(models.Model):
    name = models.CharField(max_length=50, unique=True, error_messages={'unique': 'نام درگاه تکراری است'})
    display_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    token = models.TextField(blank=True, null=True)
    active = models.BooleanField()
    wage = models.PositiveIntegerField(default=0)


class BankGatewayReceiveTransaction(models.Model):
    class Status(models.TextChoices):
        SUCCEEDED = "SUCCEEDED"
        FAILED = "FAILED"
        REQUESTED = "REQUESTED"

    class Type(models.TextChoices):
        SHAPARAK = "SHETAB"

    class Module(models.TextChoices):
        WALLET = "WALLET"

    card_number = models.CharField(max_length=24, default='')
    module = models.CharField(choices=Module.choices, db_index=True, max_length=255, default=Module.WALLET)
    type = models.CharField(choices=Type.choices, db_index=True, max_length=255)
    details = models.JSONField(default=dict)
    gateway = models.ForeignKey(
        BankGateway,
        on_delete=models.RESTRICT,
        null=True,
        blank=True,
    )
    user = models.ForeignKey(User, on_delete=models.RESTRICT, blank=True, null=True)
    amount = models.DecimalField(db_index=True, default=0, max_digits=15, decimal_places=0,
                                 validators=[MinValueValidator(0)])
    status = models.CharField(choices=Status.choices, db_index=True, max_length=255)
    desc = models.CharField(max_length=255, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
