from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.


class Hero(models.Model):
    class Type(models.TextChoices):
        STRENGTH = 'STRENGTH'
        AGILITY = 'AGILITY'
        INTELLIGENCE = 'INTELLIGENCE'
    name = models.CharField(max_length=100)
    type = models.CharField(choices=Type.choices, max_length=100, db_index=True)
    levels = models.JSONField(default=dict)
    info = models.JSONField(default=dict)
    image = models.CharField(max_length=500, null=True, blank=True)
    description = models.TextField(default='', null=True, blank=True)
    status = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def delete(self, *args, **kwargs):
        self.deleted = True
        super(Hero, self).save()


class Item(models.Model):
    class ItemType(models.TextChoices):
        SINGLE = 'SINGLE'
        SET = 'SET'
    name = models.CharField(max_length=255)
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE)
    type = models.CharField(max_length=255)
    item_price = models.DecimalField(default=0, max_digits=30, decimal_places=8, validators=[MinValueValidator(0)])
    item_type = models.CharField(choices=ItemType.choices, max_length=255, db_index=True)
    image = models.CharField(max_length=500, null=True, blank=True)
    film = models.CharField(max_length=500, null=True, blank=True)
    status = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def delete(self, *args, **kwargs):
        self.deleted = True
        super(Item, self).save()


class HeroSet(models.Model):
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item)
    set_price = models.DecimalField(default=0, max_digits=30, decimal_places=8, validators=[MinValueValidator(0)])
    image = models.CharField(max_length=500, null=True, blank=True)
    film = models.CharField(max_length=500, null=True, blank=True)
    status = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def delete(self, *args, **kwargs):
        self.deleted = True
        super(HeroSet, self).save()
