from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass 


class Post(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    post_image = models.ImageField(upload_to = "static/images/", default = "models/default.jpg")
    slug = models.SlugField(max_length=150, null=False, unique=True)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username