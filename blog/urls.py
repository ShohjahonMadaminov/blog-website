from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('', home, name='home'),
    path('<slug:slug>/about', postabout, name='about'),
    path('<slug:slug>/comment', write_comment, name='write_comment')
]