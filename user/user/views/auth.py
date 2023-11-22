from django.contrib.auth import authenticate
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import *
from rest_framework.response import Response
from rest_framework.views import APIView
from user.models import User
from user.user.serializers import UserRegisterSerializer, UserLoginSerializer


class Register(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(tags=['Auth'], request_body=UserRegisterSerializer)
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.save()
            User.hash_set_password(data, request.data['password'])
            return Response({'message': 'mission accomplished'}, status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class Login(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(tags=['Auth'], request_body=UserLoginSerializer)
    def post(self, request):
        serializer = UserLoginSerializer().create(request.data)
        if serializer['status'] is False:
            return Response(serializer, status=status.HTTP_400_BAD_REQUEST)
        auth = authenticate(username=request.data['username'], password=request.data['password'])
        if auth is not None:
            token = serializer['user'].create_token()
            return Response(token, status=status.HTTP_200_OK)
        return Response({'message': 'Your password is wrong !!!'}, status=status.HTTP_404_NOT_FOUND)


