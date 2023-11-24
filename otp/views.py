from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from otp.models import Captcha


# Create your views here.


@swagger_auto_schema(tags=['Otp'], method='GET')
@api_view(['GET'])
@permission_classes((AllowAny,))
def get_captcha(request):
    return Response(Captcha.create_captcha())
