from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Post, Profile, Relationship

# Register your models here.

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Relationship)
