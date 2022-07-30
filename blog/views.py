from django.shortcuts import redirect, render, get_object_or_404
from .models import *
from .forms import CommentForm, UserCreateForm
from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponse
from django.views.generic import CreateView
from .mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


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
    return render(request, 'blog/about.html', {'post': post, 'form':form})


def signup(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password)
            auth_login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('blog:home')
        return HttpResponse('Invalid form')
    else:
        form = UserCreateForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required(login_url='login')
def write_comment(request, slug):
    post = get_object_or_404(Post, slug = slug)
    form = CommentForm

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
    return render(request, 'blog/comment.html', {'form':form})


def login(request):
    try:
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('blog:home')
        else:
            return render(request, 'registration/login.html')
    except Exception as e:
        print(e)
        return render(request, 'registration/login.html')
    context = {
    }
    return render(request, 'registration/login.html', context)



    