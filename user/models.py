import re

from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken


# Create your models here.


class User(AbstractUser):
    phone_number = models.CharField(max_length=50, null=True, blank=True)
    national_code = models.CharField(max_length=50, null=True, blank=True)
    father_name = models.CharField(max_length=100, null=True, blank=True)
    birth_date = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.phone_number[0] == '0':
            self.phone_number = self.change_phone_number(self.phone_number)
        self.username = self.phone_number
        super().save(*args, **kwargs)

    def create_token(self):
        context = {}
        refresh = RefreshToken.for_user(self)
        context['refresh'] = str(refresh)
        context['access'] = str(refresh.access_token)
        context['message'] = 'Login was successful'
        context['is_admin'] = True if self.is_superuser else False
        return context

    @staticmethod
    def get_user_by_id(pk):
        try:
            return User.objects.get(id=pk)
        except User.DoesNotExist:
            return None

    @staticmethod
    def hash_set_password(data, password) -> None:
        data.set_password(password)
        data.save()

    @staticmethod
    def check_phone_number(phone) -> bool:
        regex = "^\\+?[1-9][0-9]{7,14}$"
        if phone[0] != '+' and phone[0] == '0':
            phone = User.change_phone_number(phone)
        elif phone[0] != '+' and phone[0] != '0':
            return False
        if len(phone) != 13:
            return False
        if phone[:3] != '+98':
            return False
        if not re.match(regex, phone):
            return False
        return True

    @staticmethod
    def change_phone_number(phone):
        return phone.replace('0', '+98', 1)
