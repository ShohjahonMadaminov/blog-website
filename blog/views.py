from django.shortcuts import render
from .models import *

def post(request):
    posts = Post.objects.all()
    return render(request, "blog/home.html", {'posts':posts})



