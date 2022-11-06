from blog_api.decorators import handle_errors
from blog_api.utils import BaseView
from core.services.auth_service import AuthService
from rest_framework import permissions, status
from rest_framework.response import Response

auth_service = AuthService()


class RegisterUserAPI(BaseView):
    @handle_errors()
    def post(self, request):
        first_name = request.data.get("first_name")
        last_name = request.data.get("last_name")
        username = request.data.get("username")
        email = request.data.get("email")
        password = request.data.get("password")

        return Response(
            {
                "data": auth_service.register_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    email=email,
                    password=password,
                )
            },
            status=status.HTTP_201_CREATED,
        )


class LoginUserAPI(BaseView):
    @handle_errors()
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        return Response(
            {"data": auth_service.login_user(username=username, password=password)},
            status=status.HTTP_200_OK,
        )


class ProfileUserAPI(BaseView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    @handle_errors()
    def get(self, request):
        return Response(
            {"data": auth_service.get_user(user_id=request.user.id)},
            status=status.HTTP_200_OK,
        )

    @handle_errors()
    def patch(self, request):
        first_name = request.data.get("first_name")
        last_name = request.data.get("last_name")
        username = request.data.get("username")
        email = request.data.get("email")
        password = request.data.get("password")

        return Response(
            {
                "data": auth_service.update_user(
                    user_id=request.user.id,
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    email=email,
                    password=password,
                )
            },
            status=status.HTTP_202_ACCEPTED,
        )
