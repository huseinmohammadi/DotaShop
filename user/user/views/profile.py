from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import *
from rest_framework.response import Response
from rest_framework.views import APIView
from user.user.serializers import ProfileSerializer


class GetMe(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(tags=['Profile'])
    def get(self, request):
        serializer = ProfileSerializer(request.user, many=False)
        return Response(serializer.data, status.HTTP_200_OK)
