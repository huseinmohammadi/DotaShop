from django.contrib.contenttypes.fields import GenericRelation
from django.core.validators import MinValueValidator
from django.db import models

from user.models import User
from wallet.models import WalletTransaction


# Create your models here.


class Order(models.Model):
    class Status(models.TextChoices):
        DONE = 'DONE'
        REQUESTED = 'REQUESTED'
        FAILED = 'FAILED'

    class Type(models.TextChoices):
        SELL = 'SELL'
        BUY = 'BUY'

    class OrderCreate(models.TextChoices):
        CLIENT = 'CLIENT'
        ADMIN = 'ADMIN'

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner_order')
    operator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='operator_order')
    total_price = models.BigIntegerField(default=0, validators=[MinValueValidator(0)])
    price_unit = models.BigIntegerField(default=0, validators=[MinValueValidator(0)])
    exchange_fee = models.FloatField(default=0)
    status = models.CharField(choices=Status.choices, null=True, blank=True, db_index=True, max_length=50)
    type = models.CharField(choices=Type.choices, null=True, blank=True, db_index=True, max_length=50)
    order_create = models.CharField(choices=OrderCreate.choices, null=True, blank=True, db_index=True, max_length=50)
    description = models.TextField(default='', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)
    wallet_transaction = GenericRelation(
        WalletTransaction,
        object_id_field="document_id",
        content_type_field="document_type",
        related_query_name='order_transaction'
    )

    def delete(self, *args, **kwargs):
        self.deleted = True
        super(Order, self).save()
