"""
Post service to help create/read posts and like a post
"""

from blog_api import exceptions
from blog_api.utils import remove_none_values
from django.shortcuts import get_object_or_404

from core.models import Like, Post
from core.serializers import PostSerializer


class PostService:
    def create_post(self, post_data):
        post_serializer = PostSerializer(data=post_data)

        if not post_serializer.is_valid():
            raise exceptions.Exception(post_serializer.errors)

        post_serializer.save()

        return post_serializer.data

    def get_all_posts(self, title=None, body=None, skip=0, limit=10):
        queryset = Post.objects.filter(
            **remove_none_values(
                {
                    "title__contains": title,
                    "body__contains": body,
                }
            )
        )[skip:limit]

        return PostSerializer(queryset, many=True).data

    def get_post(self, post_id):
        return PostSerializer(get_object_or_404(Post, id=post_id)).data

    def like_post(self, post_id):
        like = Like.objects.create(post_id=post_id)

        post = like.post
        post.likes += 1
        post.save()

        return PostSerializer(post).data
