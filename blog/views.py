from django.shortcuts import redirect, render, get_object_or_404
from .models import *
from .forms import CommentForm, UserCreateForm
from django.contrib.auth import authenticate, login


def home(request):
    category = request.GET.get('category')

    if category == None:
        posts = Post.objects.all()
    else:
        posts = Post.objects.filter(category__name = category)

    categories = Category.objects.all()
    return render(request, "blog/home.html", {'posts': posts, 'categories': categories})


def postabout(request, slug):
    form = CommentForm
    post = get_object_or_404(Post, slug = slug)

    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            com = form.save(commit=False)
            com.post = post
            com.user = request.user
            com.save()
            return redirect('blog:about', slug = post.slug)
    else:
        form = CommentForm()

    return render(request, 'blog/about.html', {'post': post, 'form':form})


def signup(request):
    # if request.user.is_anonymous:
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('first name')
            last_name = form.cleaned_data.get('last name')
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            form.save()
            new_user = authenticate(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email =email,
                password1=password1,
                password2=password2,
            )
            if new_user is not None: 
                login(request, new_user)
                return redirect('blog:home')
    # else:
    #     return redirect('blog:home')
    form = UserCreateForm
    return render(request, 'registration/signup.html', {'form':form})


