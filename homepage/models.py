from django.db import models
from django.contrib.auth.models import User


class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=75)
    title_meta = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    summary = models.TextField()
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(auto_now_add=True)


class Category(models.Model):
    title = models.CharField(max_length=75)
    meta_title = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    content = models.TextField()


class Tag(models.Model):
    title = models.CharField(max_length=75)
    meta_title = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    content = models.TextField()


class PostTag(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, blank=False, null=True)


class PostCategory(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=False, null=True)
