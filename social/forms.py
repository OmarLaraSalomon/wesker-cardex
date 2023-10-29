from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import widgets
from .models import Post
from django.contrib import admin


class UserRegisterForm(UserCreationForm):
    
    email = forms.EmailField(widget=forms.EmailInput, required=True)
    password1 = forms.CharField( 
        label='Contraseña', widget=forms.PasswordInput,required=True)
    
    password2 = forms.CharField(
        label='Confirma Contraseña', widget=forms.PasswordInput, required=True)


    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']
        help_texts = {k: "" for k in fields}


# class PostForm(forms.ModelForm):
#    content = forms.CharField(label='', widget=forms.Textarea(
#        attrs={'rows': 2, 'placeholder': '¿Qué vas a registrar?'}), required=True)

#    class Meta:
#        model = Post
#        fields = ['content']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['status', 'content', 'Fecha','entrada']
        


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': [
         'pub_date'], 'classes': ['collapse']}),
    ]
