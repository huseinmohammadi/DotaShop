from django.urls import path, include


urlpatterns = [
    path('admin/', include('user.admin.urls')),
    path('user/', include('user.user.urls')),
]
