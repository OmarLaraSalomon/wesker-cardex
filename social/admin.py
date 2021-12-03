from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Post, Profile, Relationship,Information,Egresos

# Register your models here.
admin.site.register(Relationship)

@admin.register(Profile)
class FotoAdmin(admin.ModelAdmin):
    """Profile model admin."""

    list_display = ('id', 'user')
    list_filter = ('id','user')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Profile model admin."""

    list_display = ('id', 'user','timestamp','content')
    list_filter = ('id','user')
#informacion del perfil

@admin.register(Information)
class ProfileAdmin(admin.ModelAdmin):
    """Profile model admin."""

    list_display = ('id','first_name','last_name','telefono','telefono_casa','nacimiento','direccion','contacto_emergencia','telefono_emergencia','puesto','departamento')
    list_filter = ('id', 'first_name','departamento')

@admin.register(Egresos)
class EgresoAdmin(admin.ModelAdmin):
    """Profile model admin."""

    list_display = ('id', 'user','ingreso','egreso')
    list_filter = ('id','user')


