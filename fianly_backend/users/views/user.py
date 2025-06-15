from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from typing import List, Dict

class UserListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        users: List[User] = User.objects.all()
        response: List[Dict[str, str]] = [
            {"user_name": user.first_name, "user_lastname": user.last_name}
            for user in users
        ]
        return Response(response)
