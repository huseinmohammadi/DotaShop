from django_filters import FilterSet, filters
from rest_framework import serializers
from user.models import User


class UserAdminListSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        ordering = ['-id']
        exclude = ['password']


class UserAdminFilters(FilterSet):
    phone_number = filters.CharFilter(field_name='phone_number', lookup_expr='contains')
    national_code = filters.CharFilter(field_name='national_code', lookup_expr='contains')
    father_name = filters.CharFilter(field_name='father_name', lookup_expr='contains')
    email = filters.CharFilter(field_name='email', lookup_expr='contains')
    is_superuser = filters.BooleanFilter(field_name='is_superuser', lookup_expr='exact')
    is_staff = filters.BooleanFilter(field_name='is_staff', lookup_expr='exact')
    active = filters.BooleanFilter(field_name='active', lookup_expr='exact')

    class Meta:
        model = User
        fields = ['phone_number', 'national_code', 'father_name', 'is_superuser', 'is_staff', 'active']


class UserAdminSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=False)

    class Meta:
        model = User
        exclude = ['user_permissions', 'groups', 'date_joined', 'last_login', 'username']


class UserAdminUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ['user_permissions', 'groups', 'date_joined', 'last_login', 'username', 'password', 'phone_number']


