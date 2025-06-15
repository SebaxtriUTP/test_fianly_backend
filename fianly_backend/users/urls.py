from django.urls import path
from users.views.register import RegisterView
from users.views.auth import AuthView
from users.views.user import UserListView

urlpatterns = [
    path("register", RegisterView.as_view()),
    path("auth", AuthView.as_view()),
    path("user", UserListView.as_view()),
]
