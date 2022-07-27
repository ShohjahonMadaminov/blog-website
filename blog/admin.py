from django.contrib import admin
from blog.models import Author, Category, Post, Comment, User

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)
admin.site.register(User)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Comment)
