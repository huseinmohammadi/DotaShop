from django.urls import path
from otp.views import get_captcha


urlpatterns = [
    path('captcha/', get_captcha, name='user-get-captcha'),
]
