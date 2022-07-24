from django.shortcuts import redirect, render, get_object_or_404
from .models import *
from .forms import CommentForm
from django.views.generic import DetailView


def home(request):
    category = request.GET.get('category')

    if category == None:
        posts = Post.objects.all()
    else:
        posts = Post.objects.filter(category__name = category)

    categories = Category.objects.all()
    return render(request, "blog/home.html", {'posts':posts, 'categories': categories})


def postabout(request, slug):
    form = CommentForm
    post = get_object_or_404(Post, slug = slug)
    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            com = form.save(commit=False)
            com.post = post
            com.save()
            return redirect('about/', slug = post.slug)
    else:
        form = CommentForm()

    return render(request, 'blog/about.html', {'post': post, 'form':form})
