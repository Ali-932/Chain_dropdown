from django.contrib import admin

# Register your models here.

from .models import Author, Post, Comments

admin.site.register(Author)
admin.site.register(Post)
admin.site.register(Comments)
