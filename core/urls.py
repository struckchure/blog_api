from django.urls import path

from core.api.auth_api import LoginUserAPI, ProfileUserAPI, RegisterUserAPI
from core.api.post_api import GetPostAPI, LikePostAPI, ListCreatePostAPI

post_urls = [
    path("posts/", ListCreatePostAPI.as_view(), name="create_post"),
    path("posts/<uuid:post_id>/", GetPostAPI.as_view(), name="get_post"),
    path("posts/<uuid:post_id>/like/", LikePostAPI.as_view(), name="like_post"),
]

auth_urls = [
    path("auth/register/", RegisterUserAPI.as_view(), name="register_user"),
    path("auth/login/", LoginUserAPI.as_view(), name="login_user"),
    path("auth/user/", ProfileUserAPI.as_view(), name="profile_user"),
]

urlpatterns = [
    *post_urls,
    *auth_urls,
]
