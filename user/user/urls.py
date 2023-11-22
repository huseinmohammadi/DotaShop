from django.urls import path
from user.user.views.auth import *
from user.user.views.profile import GetMe

urlpatterns = [
    path('profile/', GetMe.as_view(), name='user-getme'),
    path('register/', Register.as_view(), name='user-register'),
    path('login/', Login.as_view(), name='user-login'),
]
