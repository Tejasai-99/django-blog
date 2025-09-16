from django.contrib import admin
from .models import BlogComment, Post


admin.site.register(Post)
admin.site.register(BlogComment)