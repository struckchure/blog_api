from blog_api import exceptions
from blog_api.utils import get_object_or_raise_exception, remove_none_values
from core.serializers.auth_serializer import LoginSerializer, UserSerializer
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()


class AuthService:
    def register_user(
        self,
        first_name=None,
        last_name=None,
        username=None,
        email=None,
        password=None,
    ):
        user_register_serializer = UserSerializer(
            data=remove_none_values(
                {
                    "first_name": first_name,
                    "last_name": last_name,
                    "username": username,
                    "email": email,
                    "password": password,
                }
            )
        )

        if not user_register_serializer.is_valid():
            raise exceptions.Exception(user_register_serializer.errors)
        user_register_serializer.save(password=password)

        token = Token.objects.create(user=user_register_serializer.instance)

        return {**user_register_serializer.data, "token": token.key}

    def login_user(self, username=None, password=None):
        user_login_serializer = LoginSerializer(
            data={
                "username": username,
                "password": password,
            }
        )

        if not user_login_serializer.is_valid():
            raise exceptions.Exception(user_login_serializer.errors)
        user_login_serializer.save()

        token, _ = Token.objects.get_or_create(user=user_login_serializer.instance)

        return {**user_login_serializer.data, "token": token.key}

    def get_user(self, user_id):
        return UserSerializer(get_object_or_raise_exception(User, id=user_id)).data

    def update_user(
        self,
        user_id,
        first_name=None,
        last_name=None,
        username=None,
        email=None,
        password=None,
    ):
        user = get_object_or_raise_exception(User, id=user_id)
        user_update_serializer = UserSerializer(
            user,
            data=remove_none_values(
                {
                    "first_name": first_name,
                    "last_name": last_name,
                    "username": username,
                    "email": email,
                    "password": password,
                }
            ),
            partial=True,
        )

        if not user_update_serializer.is_valid():
            raise exceptions.Exception(user_update_serializer.errors)
        user_update_serializer.save()

        return user_update_serializer.data
