from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import UserRegisterForm, PostForm
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile
from .models import Information
from .models import DatosMedicos
from .models import AsignacionHat
from django.contrib.auth.decorators import login_required

from . import models
from django.shortcuts import render

from django.urls import reverse
from social_django.settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME, AWS_S3_REGION_NAME
import boto3 
from boto3.session import Session

    
    
def hats(request, username=None):
    template = 'social/hats.html'
    users = User.objects.all()
    asighat = AsignacionHat.objects.order_by('user_id')
    hat = Hat.objects.all()
    info = Information.objects.all()
    actividades = Actividades.objects.order_by('id')
    if request.method == 'POST':
            actividad = Actividades.objects.create(
                actividades=request.POST['actividad'], descripcion=request.POST['descripcion'], 
                hat_id=request.POST['hat_id'])
            actividad.save()

    context = {'users': users,'asighat':asighat,'hat':hat,'actividades': actividades, 'info':info}
    
    return render(request, template, context)
 
def rewards(request, username=None):
    template = 'social/rewards.html'
    users = User.objects.all()

    context = {'users': users}
    
    return render(request, template, context)    

def perfilkaisen(request, username=None):
    template = 'social/perfilkaisen.html'
    users = User.objects.all()

    context = {'users': users}
    
    return render(request, template, context)


def perfilkaisenusuario(request, username=None):
    template = 'social/perfilkaisenusuario.html'
    current_user = request.user
    if username and username != current_user.username:
        user = User.objects.get(username=username)
        posts = user.posts.all()
    else:
        posts = current_user.posts.all()
        user = current_user

    context =  {'user': user, 'posts': posts}
    
    return render(request, template, context)   

def perfilmedico(request, username=None):
    template = 'social/perfilmedico.html'
    users = User.objects.all()

    context = {'users': users}
    
    return render(request, template, context)

def perfilmedicodentro(request, username=None):
    template = 'social/perfilmedicousuario.html'
    current_user = request.user
    if username and username != current_user.username:
        user = User.objects.get(username=username)
        posts = user.posts.all()
    else:
        posts = current_user.posts.all()
        user = current_user

    context =  {'user': user, 'posts': posts}
    
    return render(request, template, context)   


def datosmedicos(request, username=None):

    if request.method == 'POST':
        if DatosMedicos.objects.filter(user_id=request.POST['user_id']).count():
            infomedica = DatosMedicos.objects.update(
                edad=request.POST['edad'], peso=request.POST['peso'], 
                estatura=request.POST['estatura'], alergias=request.POST['alergias'],
                sangre=request.POST['sangre'],enfermedad=request.POST['enfermedad'],
                lentes=request.POST['lentes'], fumas=request.POST['fumas'], 
                tomas=request.POST['tomas'], deporte=request.POST['deporte'],
                sueño=request.POST['sueño'], covid=request.POST['covid'],
                vacuna=request.POST['vacuna'],user_id=request.POST['user_id'])
            infomedica.save()
        else:
            infomedica = DatosMedicos.objects.create(
                edad=request.POST['edad'], peso=request.POST['peso'], 
                estatura=request.POST['estatura'], alergias=request.POST['alergias'],
                sangre=request.POST['sangre'],enfermedad=request.POST['enfermedad'],
                lentes=request.POST['lentes'], fumas=request.POST['fumas'], 
                tomas=request.POST['tomas'], deporte=request.POST['deporte'],
                sueño=request.POST['sueño'], covid=request.POST['covid'],
                vacuna=request.POST['vacuna'],user_id=request.POST['user_id'])
            infomedica.save()

    context = {}

    current_user = request.user
    if username and username != current_user.username:
        user = User.objects.get(username=username)
        posts = user.posts.all()
    else:
        posts = current_user.posts.all()
        user = current_user
    template = 'social/datosmedicos.html'
    
   
    return render(request, template,  {'user': user, 'posts': posts})    


def verdatosmedicos(request, username=None):
    template = 'social/verdatosmedicos.html'
    current_user = request.user
    if username and username != current_user.username:
        user = User.objects.get(username=username)
        posts = user.posts.all()
    else:
        posts = current_user.posts.all()
        user = current_user
    
    return render(request, template,  {'user': user, 'posts': posts})   
    
def perfilpsico(request, username=None):
    template = 'social/perfilpsico.html'
    users = User.objects.all()
    documents = Document.objects.all()
    context = {"files": documents, 'users': users}
    
    return render(request, template, context) 

def perfillegal(request, username=None):
    template = 'social/perfillegal.html'
    users = User.objects.all()
    legals = Documentoslegales.objects.all()
    context = {"legalfiles": legals, 'users': users}
    
    return render(request, template, context) 
#Files Psicologicos
def files(request, username=None):
    template = 'social/files.html'
    current_user = request.user
    if username and username != current_user.username:
        user = User.objects.get(username=username)
        posts = user.posts.all()
    else:
        posts = current_user.posts.all()
        user = current_user
    return render(request, template, {'user': user, 'posts': posts})
#Files Medicos
def medicfiles(request, username=None):
    template = 'social/medicfiles.html'
    current_user = request.user
    if username and username != current_user.username:
        user = User.objects.get(username=username)
        posts = user.posts.all()
    else:
        posts = current_user.posts.all()
        user = current_user
    return render(request, template, {'user': user, 'posts': posts})


#subir Kaisen
def uploadkaisen(request, username=None):
    template = 'social/perfilkaisen.html'
    users = User.objects.all()
    if request.method == "POST":
        # Fetching the form data
        fileTitle = request.POST["fileTitle"]
        uploadedFile = request.FILES["uploadedFile"]
        userid = request.POST["idField"]

        # Saving the information in the database
        kaisen = models.Kaisen(
            title = fileTitle,
            uploadedFile = uploadedFile,
            user_id = userid
            
        )
        kaisen.save()
    kaisens = models.Kaisen.objects.all()
    return render(request, template, {
        "kaisenfiles": kaisens, 'users': users })

#Files Kaisen
def kaisenfiles(request, username=None):
    template = 'social/kaisenfiles.html'
    current_user = request.user
    if username and username != current_user.username:
        user = User.objects.get(username=username)
        posts = user.posts.all()
    else:
        posts = current_user.posts.all()
        user = current_user
    return render(request, template, {'user': user, 'posts': posts})
   

#Justificantes Files
def justifyfiles(request, username=None):
    template = 'social/justifyfiles.html'
    current_user = request.user
    if username and username != current_user.username:
        user = User.objects.get(username=username)
        posts = user.posts.all()
    else:
        posts = current_user.posts.all()
        user = current_user
    return render(request, template, {'user': user, 'posts': posts})

    
def viewfiles(request, username=None):
    template = 'social/viewfiles.html'
    current_user = request.user
    if username and username != current_user.username:
        user = User.objects.get(username=username)
        posts = user.posts.all()
        documents = models.Document.objects.all()
    else:
        posts = current_user.posts.all()
        user = current_user
    return render(request, template, { 'files': documents, 'user': user, 'posts': posts})  

#Files Legales
def legalfiles(request, username=None):
    template = 'social/legalfiles.html'
    current_user = request.user
    if username and username != current_user.username:
        user = User.objects.get(username=username)
        posts = user.posts.all()
    else:
        posts = current_user.posts.all()
        user = current_user
    return render(request, template, {'user': user, 'posts': posts})

#Subir archivos a perfil Psicologico
def uploadpsico(request, username=None):
    template = 'social/files.html'
    users = User.objects.all()
    if request.method == "POST":
        
        # Fetching the form data
        fileTitle = request.POST["fileTitle"]
        uploadedFile = request.FILES["uploadedFile"]
        userid = request.POST["idField"]

        # Saving the information in the database
        document = models.Document(
            title = fileTitle,
            uploadedFile = uploadedFile,
            user_id = userid
            
        )
        document.save()

    documents = models.Document.objects.all()
    return render(request, template, {
        "files": documents, 'users': users })
    

#Subir archivos A Perfil Medico
def uploadmedic(request, username=None):
    template = 'social/perfilmedico.html'
    users = User.objects.all()
    if request.method == "POST":
        
        # Fetching the form data
        fileTitle = request.POST["fileTitle"]
        uploadedFile = request.FILES["uploadedFile"]
        userid = request.POST["idField"]

        # Saving the information in the database
        medic = models.Documentosmedicos(
            title = fileTitle,
            uploadedFile = uploadedFile,
            user_id = userid
            
        )
        medic.save()

    medics = models.Documentosmedicos.objects.all()
    return render(request, template, {
        "medicfiles": medics, 'users': users })

#Subir archivos a Justificantes Medicos 
def uploadmedicjust(request, username=None):
    template = 'social/perfilmedico.html'
    users = User.objects.all()
    if request.method == "POST":
        
        # Fetching the form data
        fileTitle = request.POST["fileTitle"]
        uploadedFile = request.FILES["uploadedFile"]
        userid = request.POST["idField"]

        # Saving the information in the database
        justificant = models.Justificantesmedicos(
            title = fileTitle,
            uploadedFile = uploadedFile,
            user_id = userid
            
        )
        justificant.save()

    justificants = models.Justificantesmedicos.objects.all()
    return render(request, template, {
        "justifyfiles": justificants, 'users': users })


#Subir archivos a perfil legal
def uploadlegal(request, username=None):
    template = 'social/perfillegal.html'
    users = User.objects.all()
    if request.method == "POST":
        
        # Fetching the form data
        fileTitle = request.POST["fileTitle"]
        uploadedFile = request.FILES["uploadedFile"]
        userid = request.POST["idField"]

        # Saving the information in the database
        legal = models.Documentoslegales(
            title = fileTitle,
            uploadedFile = uploadedFile,
            user_id = userid
            
        )
        legal.save()

    legals = models.Documentoslegales.objects.all()
    return render(request, template, {
        "legalfiles": legals, 'users': users })  

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
    hat = Hat.objects.order_by('id')
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
    context = {'hat' : hat}
    return render(request, template, context)

#Asistencias
def regasis(request, username=None):
    template = 'social/regasis.html'
    posts = Post.objects.all()

    context = {'posts': posts}

    if request.user.is_authenticated:
        current_user = request.user
        if username and username != current_user.username:
            user = User.objects.get(username=username)
            posts = user.posts.all()
        else:
            posts = current_user.posts.all()
            user = current_user
        return render(request, template, context)
    else:
        return render(request, template) 
#Fin de asistencias 

def feed(request, username=None):
    """  posts = Post.objects.all()

    context = {'posts': posts} """
    if request.user.is_authenticated:
        current_user = request.user
        if username and username != current_user.username:
            user = User.objects.get(username=username)
            posts = user.posts.all().exclude(activate = "False")
        else:
            posts = current_user.posts.all().exclude(activate = "False") 
            user = current_user
        return render(request, 'social/feed.html', {'user': user, 'posts': posts})
    else:
        return render(request, 'social/feed.html')
        


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
    for prueba in request:
        uno = request.POST['content']
        print("Vamos a traer la entrada del request" + str(prueba))
        print("Vamos a traer la entrada del request" + str(uno))
    variable = request
    for intento in variable:
        print("veremos que hay aqui"+str(intento))
    current_user = get_object_or_404(User, pk=request.user.pk)
    current_user2 = (request.user.information.first_name + " " + request.user.information.last_name  )

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.fullname = current_user2
            post.save()
            
            if uno == "entrada oficina" :
                messages.success(request, 'Asistencia registrada exitosamente!')
                return redirect('feed')
            if uno == "entrada homeofice" :
                messages.success(request, 'Entrada Home Office registrada exitosamente!')
                return redirect('feed')
            if uno == "salida oficina":
                messages.success(request, 'Salida registrada exitosamente!')
                return redirect('feed')
            if uno == "salida homeofice":
                messages.success(request, 'Salida Home Office registrada exitosamente!')
                return redirect('feed')

    else:
        form = PostForm()
    return render(request, 'social/post.html', {'form': form})


def profile(request, username=None):
    current_user = request.user
    hat = Hat.objects.order_by('id')
    registros = AsignacionHat.objects.all()
    if username and username != current_user.username:
        user = User.objects.get(username=username)
        posts = user.posts.all()
    else:
        posts = current_user.posts.all()
        user = current_user
    return render(request, 'social/profile.html', {'user': user, 'posts': posts, 'hat' : hat, 'registros' : registros})





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


def asignarhat(request):
    print(request)
    template = 'social/asignarhat.html'
    hat = Hat.objects.order_by('id')
    registros = AsignacionHat.objects.all() 

    if request.method == "POST":  
        asig = AsignacionHat.objects.create(
                  user_id=request.POST['user_id'] , hat_id = request.POST['hat_id'])
        asig.save()


    context = {'hat': hat,'registros': registros}
    return render(request, template, context)

def asistencia(request):
    template = 'social/asistencia.html'
    posts = Post.objects.all()


    context = {'posts': posts}
    return render(request,template,context)