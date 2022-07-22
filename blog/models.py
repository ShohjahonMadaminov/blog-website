from django.urls import reverse
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass 


class Category(models.Model):
     name = models.CharField(max_length=150, null=True, blank=True)

     def __str__(self):
         return self.name


class Post(models.Model):
    title = models.CharField(max_length=150, null=True, blank=True)
    description = models.TextField()
    post_image = models.ImageField(upload_to = "images/", null=True, blank=True)
    slug = models.SlugField(max_length=150, null=False, unique=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
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


