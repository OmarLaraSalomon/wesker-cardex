from dataclasses import fields
from pyexpat import model
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.fields import Field
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Document, Documentosmedicos, Kaisen, Post, Profile, Relationship,Information,Egresos, Justificantesmedicos, Documentoslegales, AsignacionHat, Hat, CredentialToken
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter
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
        fields = ('fullname','timestamp','content','status','Fecha','entrada')
        exclude = ('activate', )
        export_order = ('fullname','timestamp','content','status','Fecha','entrada')

@admin.register(Post)
class PostAdmin(ImportExportModelAdmin):
    resource_class = PostResource
    """Profile model admin."""

    list_display = ('user','timestamp','content','status','activate','Fecha','entrada')
    list_filter = (('timestamp',DateRangeFilter),('timestamp',DateTimeRangeFilter),'user','content')

class InfoResource(resources.ModelResource): 
 
    class Meta:
        model = Information
        fields = ('id','first_name','last_name','telefono','telefono_casa','nacimiento','direccion','contacto_emergencia','telefono_emergencia','puesto','departamento',)
        exclude = ('is_leader')
        export_order = ('id','first_name','last_name','telefono','telefono_casa','nacimiento','direccion','contacto_emergencia','telefono_emergencia','puesto','departamento',)


@admin.register(Information)
class ProfileAdmin(ImportExportModelAdmin):
    resource_class = InfoResource
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


#AdminKaisen
@admin.register(Kaisen)
class KaisenAdmin(admin.ModelAdmin):
    """Profile model admin."""

    list_display = ('user', 'title', 'uploadedFile', 'dateTimeOfUpload')
    list_filter = ('id','user_id')

#AdminLegal
@admin.register(Documentoslegales)
class DocumentoslegalesAdmin(admin.ModelAdmin):
    """Profile model admin."""

    list_display = ('user', 'title', 'uploadedFile', 'dateTimeOfUpload')
    list_filter = ('id','user_id')

@admin.register(AsignacionHat)
class AsignacionHat(admin.ModelAdmin):
    """Profile model admin."""

    list_display = ('create_at', 'hat_id', 'user_id')
    list_filter = ('id','user_id')

@admin.register(Hat)
class Hat(admin.ModelAdmin):
    """Profile model admin."""

    list_display = ('id','nombre_hat')

@admin.register(CredentialToken)
class CredentialToken(admin.ModelAdmin):
    """Profile model admin."""

    list_display = ('id','token', 'create_at','user_id')