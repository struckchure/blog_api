from blog_api import exceptions
from blog_api.utils import get_object_or_raise_exception, remove_none_values
from core.models import Like, Post
from core.serializers.post_serializer import CommentSerializer, PostSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class PostService:
    def create_post(self, author_id, title, body):
        author = get_object_or_raise_exception(User, id=author_id)

        post_serializer = PostSerializer(
            data={
                "author": author.id,
                "title": title,
                "body": body,
            }
        )

        if not post_serializer.is_valid():
            raise exceptions.Exception(post_serializer.errors)

        post_serializer.save()

        return post_serializer.data

    def get_all_posts(self, title=None, body=None, skip=None, limit=None):
        skip = abs(int(skip or 0))
        limit = abs(int(limit or 10))

        queryset = Post.objects.filter(
            **remove_none_values(
                {
                    "title__contains": title,
                    "body__contains": body,
                }
            )
        )[skip : skip + limit]

        return PostSerializer(queryset, many=True).data

    def get_post(self, post_id):
        return PostSerializer(get_object_or_raise_exception(Post, id=post_id)).data

    def like_post(self, user_id, post_id):
        user = get_object_or_raise_exception(User, id=user_id)
        post = get_object_or_raise_exception(Post, id=post_id)

        Like.objects.create(user=user, post=post)

        post.likes += 1
        post.save()

        return PostSerializer(post).data

    def comment_post(self, post_id, user_id, body):
        user = get_object_or_raise_exception(User, id=user_id)
        post = get_object_or_raise_exception(Post, id=post_id)

        comment_serializer = CommentSerializer(
            data={
                "post": post.id,
                "user": user.id,
                "body": body,
            }
        )

        if not comment_serializer.is_valid():
            raise exceptions.Exception(comment_serializer.errors)
        comment_serializer.save()

        post.comments += 1
        post.save()

        return PostSerializer(post).data
