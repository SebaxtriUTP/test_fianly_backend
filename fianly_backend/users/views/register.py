from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from users.validators.user_validators import register_schema
from cerberus import Validator
from typing import Dict

class RegisterView(APIView):
    def post(self, request):
        data: Dict = request.data
        validator = Validator(register_schema)

        if not validator.validate(data):
            return Response({"error_message": "Datos inválidos o incompletos"}, status=status.HTTP_400_BAD_REQUEST)

        User.objects.create_user(
            username=data["username"],
            password=data["password"],
            first_name=data["first_name"],
            last_name=data["last_name"]
        )

        return Response({"message": "Usuario creado exitosamente"}, status=status.HTTP_201_CREATED)
