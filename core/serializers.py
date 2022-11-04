from rest_framework import serializers

from core.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "title", "body", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]
