from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    phone_number = models.CharField(max_length=50, null=True, blank=True)
    national_code = models.CharField(max_length=50, null=True, blank=True)
    father_name = models.CharField(max_length=100, null=True, blank=True)
    birth_date = models.DateTimeField(null=True, blank=True)

    @staticmethod
    def get_user_by_id(pk):
        try:
            return User.objects.get(id=pk)
        except User.DoesNotExist:
            return None

    @staticmethod
    def admin_set_password(data, password) -> None:
        data.set_password(password)
        data.save()
