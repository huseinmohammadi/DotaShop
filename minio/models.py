from django.db import models
from user.models import User


# Create your models here.


class File(models.Model):
    name = models.CharField(max_length=400, unique=True)
    buket = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @staticmethod
    def create_file(name, bucket, owner):
        return File.objects.create(name=name, buket=bucket, owner=owner)

    @staticmethod
    def get_file(name, owner):
        return File.objects.get(name=name, owner=owner)

    @staticmethod
    def check_file(name, owner):
        return File.objects.filter(name=name, owner=owner).exists()

    @staticmethod
    def delete_file(name, owner):
        return File.objects.filter(name=name, owner=owner).delete()
