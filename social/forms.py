from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import widgets
from .models import Post
from django.contrib import admin


class UserRegisterForm(UserCreationForm):
    name = forms.CharField(
        label='Nombre(s)', widget=forms.TextInput, required=True)

    lastname = forms.CharField(
        label='Apellidos', widget=forms.TextInput, required=True)

    number = forms.CharField(label='Número telefónico',
                             widget=forms.TextInput, required=True)

    puesto = forms.CharField(label='Puesto',
                             widget=forms.TextInput, required=True)

    email = forms.EmailField(widget=forms.EmailInput, required=True)
    password1 = forms.CharField(
        label='Contraseña', widget=forms.PasswordInput, required=True)

    password2 = forms.CharField(
        label='Confirma Contraseña', widget=forms.PasswordInput, required=True)

    direccion = forms.CharField(
        label='Dirección', widget=forms.TextInput, required=True)

    class Meta:
        model = User
        fields = ['name', 'lastname', 'username', 'number', 'puesto', 'direccion',
                  'email', 'password1', 'password2']
        help_texts = {k: "" for k in fields}


# class PostForm(forms.ModelForm):
#    content = forms.CharField(label='', widget=forms.Textarea(
#        attrs={'rows': 2, 'placeholder': '¿Qué vas a registrar?'}), required=True)

#    class Meta:
#        model = Post
#        fields = ['content']

class PostForm(forms.ModelForm):
    content = forms.CharField(label='Favor de poner "Entrada" o "Salida" seguido de donde está trabajando "Oficina" o "HomeOffice"', required=True, widget=forms.TextInput(
        attrs={'rows': 3,  'placeholder': 'Entrada - Oficina / Salida - Oficina / Entrada - HomeOffice / Salida - HomeOffice', }))

    class Meta:
        model = Post
        fields = ['content', ]


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': [
         'pub_date'], 'classes': ['collapse']}),
    ]
