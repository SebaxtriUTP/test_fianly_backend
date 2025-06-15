from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from users.validators.user_validators import auth_schema
from cerberus import Validator
from rest_framework_simplejwt.tokens import RefreshToken
from typing import Dict

class AuthView(APIView):
    def post(self, request):
        data: Dict = request.data
        validator = Validator(auth_schema)

        if not validator.validate(data):
            return Response({"error_message": "Petición inválida"}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=data["user"], password=data["password"])
        if not user:
            return Response({"error_message": "Credenciales inválidas o usuario inexistente"}, status=status.HTTP_401_UNAUTHORIZED)

        refresh = RefreshToken.for_user(user)

        return Response({
            "token": str(refresh.access_token),
            "user_name": user.first_name
        }, status=status.HTTP_201_CREATED)
