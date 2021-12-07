from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import UserRegisterForm, PostForm
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile
from .models import Information
from django.contrib.auth.decorators import login_required



def inicio(request, username=None):
    template = 'social/dashboard.html'
    """ posts = Post.objects.all()

    context = {'posts': posts} """
    if request.user.is_authenticated:
        current_user = request.user
        if username and username != current_user.username:
            user = User.objects.get(username=username)
            posts = user.posts.all()
        else:
            posts = current_user.posts.all()
            user = current_user
            return render(request, template, {'user': user, 'posts': posts})
    else:
        return render(request, template)    


def information(request):
    print(request)
    template = 'social/information.html'
    if request.method == 'POST':
        info = Information.objects.create(
            first_name=request.POST['first_name'], last_name=request.POST['last_name'], 
            telefono=request.POST['telefono'], telefono_casa=request.POST['telefono_casa'],
            nacimiento=request.POST['nacimiento'],direccion=request.POST['direccion'],
            puesto=request.POST['puesto'], contacto_emergencia=request.POST['contacto_emergencia'], 
            telefono_emergencia=request.POST['telefono_emergencia'], departamento=request.POST['departamento'],
            user_id=request.POST['user_id'])
        info.save()
    context = {}
    return render(request, template, context)


def feed(request, username=None):
    """  posts = Post.objects.all()

     context = {'posts': posts} """
    current_user = request.user
    if username and username != current_user.username:
        user = User.objects.get(username=username)
        posts = user.posts.all()
    else:
        posts = current_user.posts.all()
        user = current_user
    return render(request, 'social/feed.html', {'user': user, 'posts': posts})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) 
      
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            return redirect('feed')
    else:
        form = UserRegisterForm()

    context = {'form': form}
    return render(request, 'social/register.html', context)


@login_required
def post(request):
    current_user = get_object_or_404(User, pk=request.user.pk)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            messages.success(request, f'{post} registrada exitosamente!')
            return redirect('feed')
    else:
        form = PostForm()
    return render(request, 'social/post.html', {'form': form})


def profile(request, username=None):
    current_user = request.user
    if username and username != current_user.username:
        user = User.objects.get(username=username)
        posts = user.posts.all()
    else:
        posts = current_user.posts.all()
        user = current_user
    return render(request, 'social/profile.html', {'user': user, 'posts': posts})


def follow(request, username):
    current_user = request.user
    to_user = User.objects.get(username=username)
    to_user_id = to_user
    rel = Relationship(from_user=current_user, to_user=to_user_id)
    rel.save()
    messages.success(request, f'Sigues a {username}')
    return redirect('feed')


def unfollow(request, username):
    current_user = request.user
    to_user = User.objects.get(username=username)
    to_user_id = to_user.id
    rel = Relationship.objects.filter(
        from_user=current_user.id, to_user=to_user_id).get()
    rel.delete()
    messages.success(request, f'Ya no sigues a {username}')
    return redirect('feed')
