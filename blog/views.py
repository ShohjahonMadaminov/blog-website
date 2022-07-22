from django.shortcuts import get_object_or_404, render
from .models import *

def home(request):
    category = request.GET.get('category')

    if category == None:
        posts = Post.objects.all()
    else:
        posts = Post.objects.filter(category__name = category)

    categories = Category.objects.all()
    return render(request, "blog/home.html", {'posts':posts, 'categories': categories})


def postabout(request, slug):
    post = get_object_or_404(Post, slug = slug)
    return render(request, 'blog/about.html', {'post': post})
