from datetime import datetime
from django.contrib import admin 
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields import EmailField
from django.utils import timezone


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

class Post(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts', null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField(choices=ENTRADAS_SALIDAS)

    class Meta:
        ordering = ['-timestamp']
    
    def clean_renewal_date(self):
        data = self.full_clean['timestamp']



class Relationship(models.Model):
    from_user = models.ForeignKey(
        User, related_name='relationships', on_delete=models.CASCADE)
    to_user = models.ForeignKey(
        User, related_name='related_to', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.from_user} to {self.to_user}'

    class Meta:
        indexes = [
            models.Index(fields=['from_user', 'to_user', ]),
        ]


class Information(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, null=True)
    first_name = models.CharField(max_length=250, null=True)
    last_name = models.CharField(max_length=250, null=True)
    telefono = models.CharField(max_length=250, null=True, unique=True)
    telefono_casa = models.CharField(max_length=250, null=True, unique=True)
    nacimiento = models.CharField(max_length=250, null=True)
    direccion = models.CharField(max_length=300, null=True)
    contacto_emergencia = models.CharField(max_length=250, null=True)
    telefono_emergencia = models.CharField(max_length=250, null=True)
    puesto = models.CharField(max_length=250, null=True)
    departamento = models.CharField(max_length=250, null=True)

   
      

class Egresos(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, null=True)
    ingreso = models.CharField(max_length=250, null=True)
    egreso = models.CharField(max_length=250, null=True)
    

