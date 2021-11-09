from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Post, Profile, Relationship,Information,Egresos

# Register your models here.

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Relationship)
#admin.site.register(Information)
class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Information, AuthorAdmin)
admin.site.register(Egresos)