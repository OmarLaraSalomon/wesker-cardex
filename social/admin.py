from dataclasses import fields
from pyexpat import model
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.fields import Field
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Document, Documentosmedicos, Post, Profile, Relationship,Information,Egresos, Justificantesmedicos, Documentoslegales

# Register your models here.
admin.site.register(Relationship)

@admin.register(Profile)
class FotoAdmin(admin.ModelAdmin):
    """Profile model admin."""

    list_display = ('id', 'user')
    list_filter = ('id','user')

class PostResource(resources.ModelResource): 
 
    class Meta:
        model = Post
        fields = ('fullname','timestamp','content',)
        exclude = ('activate', )
        export_order = ('fullname','timestamp','content',)

@admin.register(Post)
class PostAdmin(ImportExportModelAdmin):
    resource_class = PostResource
    """Profile model admin."""

    list_display = ('user','timestamp','content','activate')
    list_filter = ('timestamp','user',)

#informacion del perfil

@admin.register(Information)
class ProfileAdmin(admin.ModelAdmin):
    """Profile model admin."""

    list_display = ('id','first_name','last_name','telefono','telefono_casa','nacimiento','direccion','contacto_emergencia','telefono_emergencia','puesto','departamento','is_leader')
    list_filter = ('first_name','departamento','is_leader')

@admin.register(Egresos)
class EgresoAdmin(admin.ModelAdmin):
    """Profile model admin."""

    list_display = ('id', 'user','ingreso','egreso')
    list_filter = ('id','user')

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    """Profile model admin."""

    list_display = ('user', 'title', 'uploadedFile', 'dateTimeOfUpload')
    list_filter = ('id','user_id')
    

#AdminMedico
@admin.register(Documentosmedicos)
class DocumentosmedicosAdmin(admin.ModelAdmin):
    """Profile model admin."""

    list_display = ('user', 'title', 'uploadedFile', 'dateTimeOfUpload')
    list_filter = ('id','user_id')
    
#AdminJustificante
@admin.register(Justificantesmedicos)
class JustificantesmedicosAdmin(admin.ModelAdmin):
    """Profile model admin."""

    list_display = ('user', 'title', 'uploadedFile', 'dateTimeOfUpload')
    list_filter = ('id','user_id')

#AdminLegal
@admin.register(Documentoslegales)
class DocumentoslegalesAdmin(admin.ModelAdmin):
    """Profile model admin."""

    list_display = ('user', 'title', 'uploadedFile', 'dateTimeOfUpload')
    list_filter = ('id','user_id')