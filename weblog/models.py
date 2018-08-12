from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    post = models.CharField(max_length=500)
    title = models.CharField(max_length=200, blank=True)
    like = models.BooleanField(default=True)

    def __str__(self):
        return self.post


class Comment(models.Model):
    post = models.ForeignKey(Post, unique=False, blank=True, null=True,default=None)
    comment = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.comment
