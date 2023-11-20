from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    profile_picture = models.TextField()
    bio = models.TextField()

    def __str__(self):
        return f"User - {self.email}"


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    publication_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"BlogPosts - {self.author}"


class Comments(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    comment_content = models.TextField()

    def __str__(self):
        return f"BlogPosts - {self.blog_post}"


class Tags(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"BlogPosts - {self.blog_post}"
