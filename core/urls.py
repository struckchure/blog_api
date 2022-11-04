from django.urls import path
from core.api import ListCreatePostAPI, GetPostAPI, LikePostAPI


urlpatterns = [
    path("posts/", ListCreatePostAPI.as_view(), name="create_post"),
    path("posts/<uuid:post_id>/", GetPostAPI.as_view(), name="get_post"),
    path("posts/<uuid:post_id>/like/", LikePostAPI.as_view(), name="like_post"),
]
