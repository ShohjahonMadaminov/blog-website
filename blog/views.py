from django.shortcuts import get_object_or_404, render
from .models import *

def home(request):
    posts = Post.objects.all()
    return render(request, "blog/home.html", {'posts':posts})


def postabout(request, slug):
    post = get_object_or_404(Post, slug = slug)
    return render(request, 'blog/detail.html', {'post': post})
