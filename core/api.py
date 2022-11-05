from blog_api.decorators import handle_errors
from blog_api.utils import BaseView
from rest_framework import status
from rest_framework.response import Response

from core.service import PostService

post_service = PostService()


class ListCreatePostAPI(BaseView):
    @handle_errors()
    def get(self, request):
        title = request.query_params.get("title")
        body = request.query_params.get("body")
        skip = request.query_params.get("skip")
        limit = request.query_params.get("limit")

        return Response(
            {"data": post_service.get_all_posts(title, body, skip, limit)},
            status=status.HTTP_200_OK,
        )

    @handle_errors()
    def post(self, request):
        return Response(
            {"data": post_service.create_post(request.data)},
            status=status.HTTP_201_CREATED,
        )


class GetPostAPI(BaseView):
    @handle_errors()
    def get(self, request, post_id):
        return Response(
            {"data": self.post_service.get_post(post_id)}, status=status.HTTP_200_OK
        )


class LikePostAPI(BaseView):
    @handle_errors()
    def post(self, request, post_id):
        return Response(
            {"data": post_service.like_post(post_id)},
            status=status.HTTP_201_CREATED,
        )
