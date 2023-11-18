from django.urls import path
from user.admin.views.user import GetUsers, UserCreate, UserUpdate

urlpatterns = [
    path('list/', GetUsers.as_view(), name='user-admin-list'),
    path('create/', UserCreate.as_view(), name='user-admin-create'),
    path('update/<int:pk>/', UserUpdate.as_view(), name='user-admin-update'),
]
