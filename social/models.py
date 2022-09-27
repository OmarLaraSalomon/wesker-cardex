from datetime import datetime
from django.contrib import admin 
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields import EmailField
from django.utils import timezone

""" class Document(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, unique=False, null=True)
    title = models.CharField(max_length = 200)
    uploadedFile = models.FileField(upload_to = "Archivos Psicologicos/")
    dateTimeOfUpload = models.DateTimeField(auto_now = True) """


class Kaisen(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='actas', null=True)
    title = models.CharField(max_length = 200)
    uploadedFile = models.FileField(upload_to = "Actas Kaisen/")
    dateTimeOfUpload = models.DateTimeField(auto_now = True)

    class Meta:
        ordering = ['-dateTimeOfUpload']
        verbose_name_plural = 'kaizen'
    
    def clean_renewal_date(self):
        data = self.full_clean['dateTimeOfUpload']


class Document(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='files', null=True)
    title = models.CharField(max_length = 200)
    uploadedFile = models.FileField(upload_to = "Archivos Psicologicos/")
    dateTimeOfUpload = models.DateTimeField(auto_now = True)

    class Meta:
        ordering = ['-dateTimeOfUpload']
        verbose_name_plural = 'Documentos Psicologicos'

        
        
    
    def clean_renewal_date(self):
        data = self.full_clean['dateTimeOfUpload']

class Documentosmedicos(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='medicfiles', null=True)
    title = models.CharField(max_length = 200)
    uploadedFile = models.FileField(upload_to = "Archivos Medicos/")
    dateTimeOfUpload = models.DateTimeField(auto_now = True)

    class Meta:
        ordering = ['-dateTimeOfUpload']
        verbose_name_plural = 'Documentos Medicos'

    
    def clean_renewal_date(self):
        data = self.full_clean['dateTimeOfUpload']

class Justificantesmedicos(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='justifyfiles', null=True)
    title = models.CharField(max_length = 200)
    uploadedFile = models.FileField(upload_to = "Justificantes Medicos/")
    dateTimeOfUpload = models.DateTimeField(auto_now = True)

    class Meta:
        ordering = ['-dateTimeOfUpload']
        verbose_name_plural = 'Justificantes Medicos'
    
    def clean_renewal_date(self):
        data = self.full_clean['dateTimeOfUpload']

DOCUMENTOS = (
    ('INE','INE'),
    ('Contratos','Contratos'),
    ('Prestaciones', 'Prestaciones'),
    ('NDA', 'NDA'),
    ('Reglamento', 'Reglamento'),
    ('Priv Datos', 'Priv Datos'),
)


class Documentoslegales(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='legalfiles', null=True)
    title = models.CharField(max_length = 200)
    uploadedFile = models.FileField(upload_to = "Archivos Legales/")
    dateTimeOfUpload = models.DateTimeField(auto_now = True)

    class Meta:
        ordering = ['-dateTimeOfUpload']
        verbose_name_plural = 'Documentos Legales'
    
    def clean_renewal_date(self):
        data = self.full_clean['dateTimeOfUpload']               
    
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    image = models.ImageField(default='batman.png')
    
    def __str__(self):
            return f'Foto de perfil de { self.user.information.first_name } { self.user.information.last_name }'

    def following(self):
        user_ids = Relationship.objects.filter(from_user=self.user)\
            .values_list('to_user_id', flat=True)
        return User.objects.filter(id__in=user_ids)

    def followers(self):
        user_ids = Relationship.objects.filter(to_user=self.user)\
            .values_list('from_user_id', flat=True)
        return User.objects.filter(id__in=user_ids)

ENTRADAS_SALIDAS = (
    ('entrada oficina','ENTRADA OFICINA'),
    ('entrada homeofice','ENTRADA HOMEOFICE'),
    ('salida oficina', 'SALIDA OFICINA'),
    ('salida homeofice', 'SALIDA HOMEOFICE')
)

RETCA = (
    ('A Tiempo','A Tiempo'),
    ('Retardo','Retardo')
)

TIPO_DOC = (
    ('INE','INE'),
    ('Contrato','Contrato'),
    ('NDA', 'NDA'),
    ('Reglamento', 'Reglamento'),
    ('Priv datos', 'Priv datos'),
    ('Domicilio', 'Reglamento'),
    ('Acta nacimiento', 'Acta nacimiento')
)

class Post(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts', null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField(choices=ENTRADAS_SALIDAS)
    activate = models.BooleanField(default=True,null=True)
    fullname = models.CharField(max_length = 200,null=True)
    status = models.TextField(choices=RETCA,default=True,null=True)
    Fecha = models.CharField(max_length = 200,null=True)
    entrada = models.CharField(max_length = 200,null=True)

    class Meta:
        ordering = ['-timestamp']
        verbose_name_plural = 'Entradas/Salidas' 
    
    def clean_renewal_date(self):
        data = self.full_clean['timestamp']
    
    class MyModelAdmin(admin.ModelAdmin):
        list_display = ('datetime',)

    class MyModel(models.Model):
        datetime = models.DateTimeField(auto_now_add=True, verbose_name="Uploaded at")


class Relationship(models.Model):
    from_user = models.ForeignKey(
        User, related_name='relationships', on_delete=models.CASCADE)
    to_user = models.ForeignKey(
        User, related_name='related_to', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.from_user} to {self.to_user}'

    class Meta:

        verbose_name_plural = 'Relaciones'
        indexes = [
            models.Index(fields=['from_user', 'to_user', ]),
        ]


class Information(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, null=True)
    first_name = models.CharField(max_length=250, null=True)
    last_name = models.CharField(max_length=250, null=True)
    telefono = models.CharField(max_length=250, null=True, unique=False)
    telefono_casa = models.CharField(max_length=250, null=True,  unique=False)
    nacimiento = models.CharField(max_length=250, null=True)
    direccion = models.CharField(max_length=300, null=True)
    contacto_emergencia = models.CharField(max_length=250, null=True)
    telefono_emergencia = models.CharField(max_length=250, null=True)
    puesto = models.CharField(max_length=250, null=True)
    departamento = models.CharField(max_length=250, null=True)
    is_leader = models.BooleanField(default=False,null=True)

    class Meta:
        verbose_name_plural = 'Informacion Personal'


   
      

class Egresos(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, null=True)
    ingreso = models.CharField(max_length=250, null=True)
    egreso = models.CharField(max_length=250, null=True)

    class Meta:
        verbose_name_plural = 'Salida empresa'
    

class DatosMedicos(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, null=True)
    edad = models.CharField(max_length=250, null=True)
    peso = models.CharField(max_length=250, null=True)
    estatura = models.CharField(max_length=250, null=True)
    alergias = models.CharField(max_length=500, null=True)
    sangre = models.CharField(max_length=250, null=True)
    enfermedad = models.CharField(max_length=300, null=True)
    lentes = models.CharField(max_length=250, null=True)
    fumas = models.CharField(max_length=250, null=True)
    tomas = models.CharField(max_length=250, null=True)
    deporte = models.CharField(max_length=250, null=True)
    sueño = models.CharField(max_length=250, null=True)
    covid = models.CharField(max_length=250, null=True)
    vacuna = models.CharField(max_length=250, null=True)


class Hat(models.Model):
    nombre_hat = models.CharField(max_length=500, null=True)
    create_at = models.DateTimeField(auto_now_add=True)

class AsignacionHat(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='hats', null=True)
    hat = models.ForeignKey(
        Hat, on_delete=models.CASCADE, related_name='hats', null=True)
    create_at = models.DateTimeField(auto_now_add=True, null=True)

class Actividades(models.Model):
    actividades = models.CharField(max_length=500, null=True)
    descripcion = models.CharField(max_length=500, null=True)
    hat = models.ForeignKey(
        Hat, on_delete=models.CASCADE, related_name='actividades', null=True)
    create_at = models.DateTimeField(auto_now_add=True, null=True)

class TimestampedItem(models.Model):
    created = models.DateTimeField('created', auto_now_add=True)
    modified = models.DateTimeField('modified', auto_now=True)

class documentacion(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='documentfiles', null=True)
    TipoDocumento = models.CharField(max_length = 200)
    uploadedFile = models.FileField(upload_to = "Documentos Personales/")
    dateTimeOfUpload = models.DateTimeField(auto_now = True)
    
    class Meta:
        ordering = ['-dateTimeOfUpload']
        verbose_name_plural = 'Documentos Personales'
    
    def clean_renewal_date(self):
        data = self.full_clean['dateTimeOfUpload']