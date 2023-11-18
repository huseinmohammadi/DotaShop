from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.permissions import *
from rest_framework.response import Response
from rest_framework.views import APIView

from user.admin.serializers import UserAdminListSerializer, UserAdminFilters, UserAdminSerializer, \
    UserAdminUpdateSerializer
from user.models import User
from utils.api_pagination import Pagination


class GetUsers(generics.ListAPIView):
    permission_classes = (IsAdminUser, IsAuthenticated)
    serializer_class = UserAdminListSerializer
    pagination_class = Pagination
    filterset_class = UserAdminFilters

    @swagger_auto_schema(tags=['Admin User'])
    def get(self, request, *args, **kwargs):
        return super().get(request, args, kwargs)

    def get_queryset(self):
        return User.objects.all()


class UserCreate(APIView):
    permission_classes = (IsAdminUser, IsAuthenticated)

    @swagger_auto_schema(tags=['Admin User'], request_body=UserAdminSerializer)
    def post(self, request):
        serializer = UserAdminSerializer(data=request.data)
        password = request.data['password']
        del request.data['password']
        if serializer.is_valid():
            data = serializer.save()
            User.admin_set_password(data, password)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def get_user_objects(pk):
    if (user := User.get_user_by_id(pk)) is None:
        return Http404
    return user


class UserUpdate(APIView):
    permission_classes = (IsAdminUser, IsAuthenticated)

    @swagger_auto_schema(tags=['Admin User'], request_body=UserAdminUpdateSerializer)
    def put(self, request, pk):
        user = get_user_objects(pk)
        serializer = UserAdminUpdateSerializer(user, data=request.data)
        password = request.data['password']
        del request.data['password']
        if serializer.is_valid():
            serializer.save()
            User.admin_set_password(user, password)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(tags=['Admin User'])
    def delete(self, request, pk):
        user = get_user_objects(pk)
        user.delete()
        return Response({'message': 'deleted user'}, status=status.HTTP_200_OK)
