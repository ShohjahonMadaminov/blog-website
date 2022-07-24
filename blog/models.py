from django.urls import reverse
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_admin = models.BooleanField(default=True)
    is_user = models.BooleanField(default=False)

class Category(models.Model):
     name = models.CharField(max_length=150, null=True, blank=True)

     def __str__(self):
         return self.name


class Post(models.Model):
    title = models.CharField(max_length=150, null=True, blank=True)
    description = models.TextField()
    post_image = models.ImageField(upload_to = "images/", null=True, blank=True)
    slug = models.SlugField(max_length=150, null=False, unique=True, blank=True)
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE, null=True, blank=True)
    author = models.ForeignKey('Author', on_delete=models.CASCADE, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:about', kwargs={'slug':self.slug})


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.user.username


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.DateField(auto_now_add=True)
    post = models.ForeignKey(Post, related_name='comments',on_delete=models.CASCADE, blank=True, null=True)
    content = models.TextField()

    def __str__(self):
        return self.is_admin