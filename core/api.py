from blog_api.utils import BaseView
from rest_framework import status
from rest_framework.response import Response

from core.service import PostService

post_service = PostService()


class ListCreatePostAPI(BaseView):
    def get(self, request):
        return Response(
            {"data": post_service.get_all_posts()}, status=status.HTTP_200_OK
        )

    def post(self, request):
        try:
            return Response(
                {"data": post_service.create_post(request.data)},
                status=status.HTTP_201_CREATED,
            )
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class GetPostAPI(BaseView):
    def get(self, request, post_id):
        return Response(
            {"data": self.post_service.get_post(post_id)}, status=status.HTTP_200_OK
        )


class LikePostAPI(BaseView):
    def post(self, request, post_id):
        try:
            return Response(
                {"data": post_service.like_post(post_id)},
                status=status.HTTP_201_CREATED,
            )
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
