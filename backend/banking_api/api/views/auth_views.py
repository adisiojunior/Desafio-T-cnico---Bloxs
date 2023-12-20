# api/views/auth_views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.permissions import AllowAny

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Credenciais inválidas'}, status=status.HTTP_401_UNAUTHORIZED)


class CustomTokenObtainPairView(TokenObtainPairView):
    permission_classes = [AllowAny]

class CustomTokenRefreshView(TokenRefreshView):
    pass