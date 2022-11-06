from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers, status
from django.utils import timezone

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        required=True, write_only=True, style={"input_type": "password"}
    )

    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "username",
            "email",
            "password",
            "last_login",
            "date_joined",
        ]

    def create(self, validated_data):
        password = validated_data.get("password")

        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()

        return user


class LoginSerializer(serializers.Serializer):

    username = serializers.CharField(required=True)
    password = serializers.CharField(
        required=True,
        write_only=True,
        style={"input_type": "password"},
    )

    def create(self, validated_data):
        user = authenticate(**validated_data)

        if not user:
            raise serializers.ValidationError(
                "Invalid username or password.",
                code=status.HTTP_401_UNAUTHORIZED,
            )

        user.last_login = timezone.now()
        user.save()

        return user

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.username = validated_data.get("username", instance.username)
        instance.email = validated_data.get("email", instance.email)

        password = validated_data.pop("password")
        instance.set_password(password)
        instance.save()

        return instance
