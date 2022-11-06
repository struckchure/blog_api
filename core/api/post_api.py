from blog_api.decorators import handle_errors
from blog_api.utils import BaseView
from core.services.post_service import PostService
from rest_framework import permissions, status
from rest_framework.response import Response

post_service = PostService()


class ListCreatePostAPI(BaseView):

    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
    ]

    @handle_errors()
    def get(self, request):
        title = request.query_params.get("title")
        body = request.query_params.get("body")
        skip = request.query_params.get("skip")
        limit = request.query_params.get("limit")

        return Response(
            {
                "data": post_service.get_all_posts(
                    title=title,
                    body=body,
                    skip=skip,
                    limit=limit,
                )
            },
            status=status.HTTP_200_OK,
        )

    @handle_errors()
    def post(self, request):
        author_id = request.user.id
        title = request.data.get("title")
        body = request.data.get("body")

        return Response(
            {
                "data": post_service.create_post(
                    author_id=author_id,
                    title=title,
                    body=body,
                )
            },
            status=status.HTTP_201_CREATED,
        )


class GetPostAPI(BaseView):
    @handle_errors()
    def get(self, request, post_id):
        return Response(
            {"data": post_service.get_post(post_id=post_id)},
            status=status.HTTP_200_OK,
        )


class LikePostAPI(BaseView):

    permission_classes = [
        permissions.IsAuthenticated,
    ]

    @handle_errors()
    def post(self, request, post_id):
        user_id = request.user.id

        return Response(
            {
                "data": post_service.like_post(
                    user=user_id,
                    post_id=post_id,
                )
            },
            status=status.HTTP_201_CREATED,
        )


class CommentPostAPI(BaseView):

    permission_classes = [
        permissions.IsAuthenticated,
    ]

    @handle_errors()
    def post(self, request, post_id):
        user_id = request.user.id
        body = request.data.body

        return Response(
            {
                "data": post_service.comment_post(
                    post_id=post_id,
                    user_id=user_id,
                    body=body,
                )
            },
            status=status.HTTP_201_CREATED,
        )
