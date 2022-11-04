from blog_api.utils import BaseModel
from django.db import models


class Post(BaseModel):
    title = models.CharField(max_length=255)
    body = models.TextField()
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Like(BaseModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.post.title} - {self.created_at}"
