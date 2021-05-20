from django.contrib import admin
from .models import Blog, Comment, Category

admin.site.register(Blog),
admin.site.register(Comment),
admin.site.register(Category),