from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import UserRegisterForm, PostForm
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile
from .models import Information
from .models import DatosMedicos
from .models import AsignacionHat
from .models import documentacion
from .models import contratacion
from .models import CredentialToken
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect
from . import models
from django import template
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse
from social_django.settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME, AWS_S3_REGION_NAME
import boto3 
from boto3.session import Session
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
import qrcode
from io import BytesIO
from django.core.exceptions import ObjectDoesNotExist
from dateutil.relativedelta import relativedelta
from datetime import datetime  # Asegúrate de tener esta importación en la parte superior de tu archivo
    
    
def hats(request, username=None):
    template = 'social/hats.html'
    users = User.objects.all().exclude(is_active = "False")
    
    search_query = request.GET.get('search')
    if search_query:
        users = users.filter(
            Q(username__icontains=search_query) |  # Buscar en el nombre de usuario
            Q(first_name__icontains=search_query) |  # Buscar en el nombre
            Q(last_name__icontains=search_query) |  # Buscar en el apellido
            Q(information__departamento__icontains=search_query)  # Buscar en el departamento
        )
    
    paginator = Paginator(users, 15)  # 10 registros por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    page_num = page_obj.number
    max_pages_before_and_after = 2
    page_numbers = [num for num in range(page_num - max_pages_before_and_after, page_num + max_pages_before_and_after + 1) if 1 <= num <= page_obj.paginator.num_pages]
    
    context = {'users': page_obj,'page_numbers': page_numbers}
    
    return render(request, template, context)
 
def rewards(request, username=None):
    template = 'social/rewards.html'
    users = User.objects.all().exclude(is_active = "False")

    context = {'users': users}
    
    return render(request, template, context)    

def cartas(request):
    template = 'social/docs.html'
    users = User.objects.all().exclude(is_active = "False")
    
    search_query = request.GET.get('search')
    if search_query:
        users = users.filter(
            Q(username__icontains=search_query) |  # Buscar en el nombre de usuario
            Q(first_name__icontains=search_query) |  # Buscar en el nombre
            Q(last_name__icontains=search_query) |  # Buscar en el apellido
            Q(information__departamento__icontains=search_query)  # Buscar en el departamento
        )
    
    paginator = Paginator(users, 15)  # 10 registros por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    page_num = page_obj.number
    max_pages_before_and_after = 2
    page_numbers = [num for num in range(page_num - max_pages_before_and_after, page_num + max_pages_before_and_after + 1) if 1 <= num <= page_obj.paginator.num_pages]
    
    context = {'users': page_obj,'page_numbers': page_numbers}
    
    return render(request, template, context)

def constancia (request, username=None):
    user = username
    us1= User.objects.get(username=user)
    template = 'social/constancia.html'
    context = {'us1':us1}
    
    return render(request, template, context)

def renuncia (request, username=None):
    user = username
    us1= User.objects.get(username=user)
    template = 'social/renuncia.html'
    context = {'us1':us1}
    
    return render(request, template, context)

def finiquito (request, username=None):
    user = username
    us1= User.objects.get(username=user)
    template = 'social/finiquito.html'
    context = {'us1':us1}
    
    return render(request, template, context)

def perfilkaisen(request, username=None):
    template = 'social/perfilkaisen.html'
    users = User.objects.all().exclude(is_active = "False")
    search_query = request.GET.get('search')
    if search_query:
        users = users.filter(
            Q(username__icontains=search_query) |  # Buscar en el nombre de usuario
            Q(first_name__icontains=search_query) |  # Buscar en el nombre
            Q(last_name__icontains=search_query) |  # Buscar en el apellido
            Q(information__departamento__icontains=search_query)  # Buscar en el departamento
        )
    
    paginator = Paginator(users, 15)  # 10 registros por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    page_num = page_obj.number
    max_pages_before_and_after = 2
    page_numbers = [num for num in range(page_num - max_pages_before_and_after, page_num + max_pages_before_and_after + 1) if 1 <= num <= page_obj.paginator.num_pages]


    context = {'users': page_obj, 'page_numbers': page_numbers}
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
    users = User.objects.all().exclude(is_active = "False")

    search_query = request.GET.get('search')
    if search_query:
        users = users.filter(
            Q(username__icontains=search_query) |  # Buscar en el nombre de usuario
            Q(first_name__icontains=search_query) |  # Buscar en el nombre
            Q(last_name__icontains=search_query) |  # Buscar en el apellido
            Q(information__departamento__icontains=search_query)  # Buscar en el departamento
        )
    
    paginator = Paginator(users, 15)  # 10 registros por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    page_num = page_obj.number
    max_pages_before_and_after = 2
    page_numbers = [num for num in range(page_num - max_pages_before_and_after, page_num + max_pages_before_and_after + 1) if 1 <= num <= page_obj.paginator.num_pages]


    context = {'users': page_obj, 'page_numbers': page_numbers}
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
        medical= DatosMedicos.objects.get(user_id=request.POST['user_id'])
        medical.edad=request.POST['edad']
        medical.peso=request.POST['peso']
        medical.estatura=request.POST['estatura']
        medical.alergias=request.POST['alergias']
        medical.sangre=request.POST['sangre']
        medical.enfermedad=request.POST['enfermedad']
        medical.lentes=request.POST['lentes']
        medical.fumas=request.POST['fumas']
        medical.tomas=request.POST['tomas']
        medical.deporte=request.POST['deporte']
        medical.sueño=request.POST['sueño']
        medical.covid=request.POST['covid']
        medical.vacuna=request.POST['vacuna']
        medical.save()
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
    if request.method == 'POST':
        infomedica = DatosMedicos.objects.create(
                edad=request.POST['edad'], peso=request.POST['peso'], 
                estatura=request.POST['estatura'], alergias=request.POST['alergias'],
                sangre=request.POST['sangre'],enfermedad=request.POST['enfermedad'],
                lentes=request.POST['lentes'], fumas=request.POST['fumas'], 
                tomas=request.POST['tomas'], deporte=request.POST['deporte'],
                sueño=request.POST['sueño'], covid=request.POST['covid'],
                vacuna=request.POST['vacuna'],user_id=request.POST['user_id'])
        infomedica.save()

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
    users = User.objects.all().exclude(is_active = "False")
    documents = Document.objects.all()
    search_query = request.GET.get('search')
    if search_query:
        users = users.filter(
            Q(username__icontains=search_query) |  # Buscar en el nombre de usuario
            Q(first_name__icontains=search_query) |  # Buscar en el nombre
            Q(last_name__icontains=search_query) |  # Buscar en el apellido
            Q(information__departamento__icontains=search_query)  # Buscar en el departamento
        )
    
    paginator = Paginator(users, 15)  # 10 registros por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    page_num = page_obj.number
    max_pages_before_and_after = 2
    page_numbers = [num for num in range(page_num - max_pages_before_and_after, page_num + max_pages_before_and_after + 1) if 1 <= num <= page_obj.paginator.num_pages]

    context = {"files": documents, 'users': page_obj, 'page_numbers': page_numbers}
    
    return render(request, template, context) 

def perfillegal(request, id=None):
    user_id2=id
    template = 'social/perfillegal.html'
    registros = AsignacionHat.objects.filter(user_id=user_id2) #variable para comparar el hat de la cuenta
    users = User.objects.all().exclude(is_active = "False") #obtiene todos los usuarios
    tiene_permiso = registros.filter(hat_id__in=[42, 22]).exists()
    legals = Documentoslegales.objects.all() 
    documentoP = documentacion.objects.all()
    
    search_query = request.GET.get('search')
    if search_query:
        users = users.filter(
            Q(username__icontains=search_query) |  # Buscar en el nombre de usuario
            Q(first_name__icontains=search_query) |  # Buscar en el nombre
            Q(last_name__icontains=search_query) |  # Buscar en el apellido
            Q(information__departamento__icontains=search_query)  # Buscar en el departamento
        )
    
    paginator = Paginator(users, 10)  # 10 registros por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    page_num = page_obj.number
    max_pages_before_and_after = 2
    page_numbers = [num for num in range(page_num - max_pages_before_and_after, page_num + max_pages_before_and_after + 1) if 1 <= num <= page_obj.paginator.num_pages]
    context = {"legalfiles": legals, 'users': page_obj,"documentoP": documentoP,'registros':registros, 'page_numbers': page_numbers, 'tiene_permiso': tiene_permiso, "userid": user_id2}
    
    return render(request, template, context) 
#Files Psicologicos
def files(request, username=None):
    template = 'social/files.html'
    if request.method  == 'POST':
        print(request.POST['name']) 
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
    users = User.objects.all().exclude(is_active = "False")
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

# Subir archivos a perfil Psicologico
def uploadpsico(request, username=None):
    template = 'social/files.html'
    users = User.objects.all().exclude(is_active="False")

    if request.method == "POST":
        # Fetching the form data
        fileTitle = request.POST["fileTitle"]
        uploadedFile = request.FILES["uploadedFile"]
        userid = request.POST["idField"]

        try:
          
            document = models.Document(
                title=fileTitle,
                uploadedFile=uploadedFile,
                user_id=userid
            )
            document.save()
            messages.success(request, "El archivo se ha guardado exitosamente.")
            return redirect('perfilpsico')
        except Exception as e:
            messages.error(request, "Hubo un error al guardar el archivo.")

    documents = models.Document.objects.all()
    return render(request, template, {
        "files": documents, 'users': users })

def legalDocumentos(request, username=None):
    template = 'social/legalDocumentos.html'
    documentoP = documentacion.objects.all()
    current_user = request.user
    if username and username != current_user.username:
        user = User.objects.get(username=username)
    else:
        user = current_user

    context = {'user': user, 'documentoP': documentoP}
    return render(request, template, context)

def subirdocumentacion(request):
    users = User.objects.all().exclude(is_active = "False")
    legals = Documentoslegales.objects.all()
    documentoP = documentacion.objects.all()
    registros = AsignacionHat.objects.all()
    hat = Hat.objects.order_by('id')
    if request.method == "POST":
        # Fetching the form data
        TipoDocumento = request.POST["TipoDocumento"]
        uploadedFile = request.FILES["uploadedFile"]
        userid = request.POST["userid"]
        # Saving the information in the database
        documento1 = models.documentacion(
            TipoDocumento = TipoDocumento,
            uploadedFile = uploadedFile,
            user_id = userid,
            
        )
        documento1.save()
        context = {'users': users, 'legals' : legals, 'documentoP': documentoP,'registros':registros,'hat':hat}
    return render(request, 'social/perfillegal.html', context)

def inclusiondocumentos(request, username=None):
    template = 'social/inclusiondocumentos.html'
    documentoP = documentacion.objects.all()
    current_user = request.user
    if username and username != current_user.username:
        user = User.objects.get(username=username)
    else:
        user = current_user

    context = {'user': user, 'documentoP': documentoP}
    return render(request, template, context)

def subirinclusion(request):
    users = User.objects.all().exclude(is_active = "False")
    legals = Documentoslegales.objects.all()
    documentoP = documentacion.objects.all()
    registros = AsignacionHat.objects.all()
    hat = Hat.objects.order_by('id')
    if request.method == "POST":
        # Fetching the form data
        TipoDocumento = request.POST["TipoDocumento"]
        uploadedFile = request.FILES["uploadedFile"]
        userid = request.POST["userid"]
        # Saving the information in the database
        documento1 = models.documentacion(
            TipoDocumento = TipoDocumento,
            uploadedFile = uploadedFile,
            user_id = userid,
            
        )
        documento1.save()
         # En lugar de redirigir, envía una respuesta JSON de éxito
        response_data = {'success': True}
        return JsonResponse(response_data)
    

#Subir archivos A Perfil Medico
def uploadmedic(request, username=None):
    template = 'social/perfilmedico.html'
    users = User.objects.all().exclude(is_active = "False")
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
    users = User.objects.all().exclude(is_active = "False")
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
    users = User.objects.all().exclude(is_active = "False")
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
    """ html_template = loader.get_template('home/index.html') """
    if request.user.is_authenticated:
        current_user = request.user
        if username and username != current_user.username:
            user = User.objects.get(username=username)
            posts = user.posts.all().exclude(activate = "False")
            
        else:
            posts = current_user.posts.all().exclude(activate = "False")
            user = current_user
            
            
        paginator = Paginator(posts, 10)  # 10 registros por página
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        page_num = page_obj.number
        max_pages_before_and_after = 2
        page_numbers = [num for num in range(page_num - max_pages_before_and_after, page_num + max_pages_before_and_after + 1) if 1 <= num <= page_obj.paginator.num_pages]

        return render(request, template, {'user': user, 'posts': page_obj, 'page_numbers': page_numbers})
    else:
        return render(request, template)    


# para lo del token
from django.utils.crypto import get_random_string


def information(request):
    hat = Hat.objects.order_by('id')
    template = 'social/information.html'

    if request.method == 'POST':
        # Obtiene el usuario actualmente autenticado
        user = request.user
        

   # Intenta obtener el objeto Information del usuario o crear uno nuevo si no existe
        # Verifica si existe un registro de Information con ese usuario
        info, created = Information.objects.get_or_create(user=user)
#este es pra querr me cree varios objetos y los actualice sin que se generen mas registros 

        # Actualiza la información del usuario del objeto info 
        info.first_name = request.POST['first_name']
        info.last_name = request.POST['last_name']
        info.telefono = request.POST['telefono']
        info.telefono_casa = request.POST['telefono_casa']
        info.nacimiento = request.POST['nacimiento']
        info.direccion = request.POST['direccion']
        info.puesto = request.POST['puesto']
        info.contacto_emergencia = request.POST['contacto_emergencia']
        info.telefono_emergencia = request.POST['telefono_emergencia']
        info.departamento = request.POST['departamento']
        info.save()

        # Genera y guarda el token automáticamente
        toke, created = CredentialToken.objects.get_or_create(user=user)
        if created or not toke.token:
            toke.token = get_random_string(length=20)
            toke.save()
            messages.success(request, "Actualización de Perfil Correctamente")
            print("El token generado es:", toke)

        # Redirige al usuario a la página 'profile' después de procesar el formulario
        return redirect('profile')

    context = {'hat': hat}
    return render(request, template, context)

#Asistencias
def regasis(request, username=None):
    template = 'social/regasis.html'
    posts = Post.objects.all()
    if request.user.is_authenticated:
        current_user = request.user
        if username and username != current_user.username:
            user = User.objects.get(username=username)
            posts = user.posts.all()
        else:
            posts = current_user.posts.all()
            user = current_user
            
        search_query = request.GET.get('search')
        if search_query:
                 posts = posts.filter(
                    Q(content__icontains=search_query) |
                    Q(fullname__icontains=search_query) |
                    Q(status__icontains=search_query) |
                    Q(Fecha__icontains=search_query) |
                    Q(entrada__icontains=search_query)
                    )
            
        paginator = Paginator(posts, 10)  # 10 registros por página
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        page_num = page_obj.number
        max_pages_before_and_after = 2
        page_numbers = [num for num in range(page_num - max_pages_before_and_after, page_num + max_pages_before_and_after + 1) if 1 <= num <= page_obj.paginator.num_pages]

        context = {'posts': page_obj, 'user': user, 'page_numbers': page_numbers}
            
        return render(request, template, context)
    else:
        return render(request, template) 
#Fin de asistencias 

def feed(request, username=None):
    if request.user.is_authenticated:
        current_user = request.user
        if username and username != current_user.username:
            user = User.objects.get(username=username)
            posts = user.posts.all().exclude(activate = "False")
            
        else:
            posts = current_user.posts.all().exclude(activate = "False") 
            user = current_user
            
        paginator = Paginator(posts, 10)  # 10 registros por página
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        page_num = page_obj.number
        max_pages_before_and_after = 2
        page_numbers = [num for num in range(page_num - max_pages_before_and_after, page_num + max_pages_before_and_after + 1) if 1 <= num <= page_obj.paginator.num_pages]

        return render(request, 'social/feed.html', {'user': user, 'posts': page_obj, 'page_numbers': page_numbers})
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
    
    dias_transcurridos = None #para manejar el caso en que no haya un período definido
    anios_transcurridos = None
    meses_transcurridos = None
    
    dias_transcurridos_actual = None #para manejar el caso en que no haya un período definido
    anios_transcurridos_actual = None
    meses_transcurridos_actual = None
    tiempo_transcurrido_hasta_ahora= None
    tiempo_formateado = None  # Definir tiempo_formateado como None
    
    if username: #verifica si existe username 
        try:
            user = User.objects.get(username=username) #esto re cupera el username de la url 
        except User.DoesNotExist:
            user = None #si no existe es none 
    else: #si username no tiene valor va acceder al usuario actual que seria el que inicio sesion 
        user = current_user

    periodo = Egresos.objects.filter(user=user).first() #me filtra por usuario y ya no por la sesion actual
    if periodo and periodo.ingreso: #verifica si ya existe el periodo
        try:
            fecha_ingreso = timezone.make_aware(datetime.strptime(periodo.ingreso, '%Y-%m-%d'), timezone.utc)
            fecha_actual= timezone.now()
            
            diferencia_actual=relativedelta(fecha_actual, fecha_ingreso)
            anios_transcurridos_actual = diferencia_actual.years
            meses_transcurridos_actual = diferencia_actual.months
            dias_transcurridos_actual = diferencia_actual.days
            print("Años (hasta ahora):", anios_transcurridos_actual)
            print("Meses (hasta ahora):", meses_transcurridos_actual)
            print("Días (hasta ahora):", dias_transcurridos_actual)
            tiempo_transcurrido_hasta_ahora = fecha_actual - fecha_ingreso
            print("Tiempo transcurrido hasta ahora:", tiempo_transcurrido_hasta_ahora)
            
            
            dias = tiempo_transcurrido_hasta_ahora.days
            horas, segundos = divmod(tiempo_transcurrido_hasta_ahora.seconds, 3600)
            minutos, segundos = divmod(segundos, 60)
            
            tiempo_formateado = {
                'dias': dias,
                'horas': horas,
                'minutos': minutos,
                'segundos': segundos,
            }
            
            if periodo.egreso:  # Si hay egreso, calcula la diferencia de tiempo con egreso
                fecha_egreso = timezone.make_aware(datetime.strptime(periodo.egreso, '%Y-%m-%d'), timezone.utc)
                diferencia = relativedelta(fecha_egreso, fecha_ingreso)
                anios_transcurridos = diferencia.years #años  dividiendo la cantidad total de días por 365
                meses_transcurridos = diferencia.months #meses dividiendo el residuo de los días por 365 entre 31 
                dias_transcurridos = diferencia.days #días  dividiendo el residuo de los días por 365 entre 31
    
                print("Años (con egreso):", anios_transcurridos)
                print("Meses (con egreso):", meses_transcurridos)
                print("Días (con egreso):", dias_transcurridos)
            
            
        except ValueError as e: #excepciones
            print("Error al convertir las fechas:", e)
    
    if username and username != current_user.username:
        user = User.objects.get(username=username)
        posts = user.posts.all()
        asignados = AsignacionHat.objects.filter(user_id=user.id)
        cantidad_registros = asignados.count()
        print(cantidad_registros)
    else:
        posts = current_user.posts.all()
        user = current_user
        asignados = AsignacionHat.objects.filter(user_id=current_user.id)
        cantidad_registros = asignados.count()
    return render(request, 'social/profile.html', {
        'user': user,  'posts': posts, 'hat' : hat, 'registros' : asignados, 
        'cantidad_registros': cantidad_registros , 
        'periodo': periodo, 
        'tiempo_formateado': tiempo_formateado,
        'dias_transcurridos': dias_transcurridos, 
        'anios_transcurridos': anios_transcurridos,
        'meses_transcurridos': meses_transcurridos, 
        'tiempo_transcurrido_hasta_ahora': tiempo_transcurrido_hasta_ahora,
        'dias_transcurridos_actual': dias_transcurridos_actual,
        'anios_transcurridos_actual': anios_transcurridos_actual,
        'meses_transcurridos_actual': meses_transcurridos_actual,
    })

@login_required
def asignaregreso(request, user_id=None):
    template = 'social/asignar_egreso.html'
   
    id_user=user_id
   
    periodo_existente = Egresos.objects.filter(user_id=id_user).first()
   
    if request.method == 'POST':
        ingreso = request.POST.get('ingreso', None)
        egreso = request.POST.get('egreso', None)
        id = request.POST.get('id', None)
      
        if periodo_existente:
            # Solo actualiza la fecha de ingreso si se proporciona una nueva fecha
            if ingreso:
                periodo_existente.ingreso = ingreso
            periodo_existente.egreso = egreso if egreso else None
            periodo_existente.save()
            messages.success(request, "Periodo actualizado con éxito")
        else:
            Egresos.objects.create(
                user_id=id_user,
                ingreso=ingreso,
                egreso=egreso if egreso else None
        
            )
            messages.success(request, "Periodo asignado con éxito")

        return redirect('profile')

    context = {'periodo_existente': periodo_existente, 'id_user':id_user}
    return render(request, template, context)

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
    posts = Post.objects.filter(activate=True)
    users = User.objects.all()
    
    search_query = request.GET.get('search')
    if search_query:
                 posts = posts.filter(
                    Q(content__icontains=search_query) |
                    Q(fullname__icontains=search_query) |
                    Q(status__icontains=search_query) |
                    Q(Fecha__icontains=search_query) |
                    Q(entrada__icontains=search_query)
                    )
            
    paginator = Paginator(posts, 10)  # 10 registros por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    page_num = page_obj.number
    max_pages_before_and_after = 2
    page_numbers = [num for num in range(page_num - max_pages_before_and_after, page_num + max_pages_before_and_after + 1) if 1 <= num <= page_obj.paginator.num_pages]

    context = {'posts': page_obj,'users': users, 'page_numbers': page_numbers}
    return render(request,template,context)

def credencial(request, tokenid=None):
    template = 'social/credencial.html'
    token1= tokenid
    token2 = CredentialToken.objects.get(token=token1)
    usuario = token2.user_id
    print(usuario)
    user = User.objects.get(id=token2.user_id)
    puesto = AsignacionHat.objects.filter(user_id=usuario)
    hats = Hat.objects.all()
    context = {'user': user, 'puesto': puesto, 'hats':hats}
    return render(request, template, context)

def credencial_fisica(request):
    template = "social/credencial_fisica.html"
    users = User.objects.all().exclude(is_active = "False")
    search_query = request.GET.get('search')
    if search_query:
        users = users.filter(
            Q(username__icontains=search_query) |  # Buscar en el nombre de usuario
            Q(first_name__icontains=search_query) |  # Buscar en el nombre
            Q(last_name__icontains=search_query) |  # Buscar en el apellido
            Q(information__departamento__icontains=search_query)  # Buscar en el departamento
        )
        
    paginator = Paginator(users, 15)  # 10 registros por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    page_num = page_obj.number
    max_pages_before_and_after = 2
    page_numbers = [num for num in range(page_num - max_pages_before_and_after, page_num + max_pages_before_and_after + 1) if 1 <= num <= page_obj.paginator.num_pages]

    context = {'users': page_obj,'page_numbers': page_numbers}

    return render(request, template, context)


def ver(request, id):
    
    u = User.objects.get(id = id)
    user = User.objects.all().filter(id = id)
    inf = Information.objects.get(user_id = u)
    # mejorar este if
    if inf.departamento == "Agua":
        template = "social/credenciales/agua.html"
    elif inf.departamento == "Aire":
        template = "social/credenciales/aire.html"
    elif inf.departamento == "Dabba":
        template = "social/credenciales/dabba.html"
    elif inf.departamento == "Ether":
        template = "social/credenciales/eter.html"
    elif inf.departamento == "Fuego":
        template = "social/credenciales/fuego.html"
    elif inf.departamento == "Ignis":
        template = "social/credenciales/ignis.html"
    elif inf.departamento == "Digimundo":
        template = "social/credenciales/digimundo.html"
    elif inf.departamento == "Tierra":
        template = "social/credenciales/tierra.html"
    
    context = {"u": user}
    return render(request, template, context)



def contrataciones(request):
    registros = contratacion.objects.all()
    asignacion = AsignacionHat.objects.all()
    users = User.objects.all().exclude(is_active = "False")
    hat = Hat.objects.order_by('id')
    
    context = {'registros': registros, 'asignacion':asignacion, 'users':users, 'hat':hat}
    return render(request, 'social/contrataciones.html',context)

def subircontratacion(request):
    registros = contratacion.objects.all()
    asignacion = AsignacionHat.objects.all()
    users = User.objects.all().exclude(is_active = "False")
    hat = Hat.objects.order_by('id')
    
    if request.method == "POST":
        # Fetching the form data
        aspirante = request.POST["nombreID"]
        uploadedNotes = request.FILES["uploadedFileCV"]
        uploadedCV = request.FILES["uploadedFile"]
        contratado = request.POST["statusContratacion"]
        Comentarios = request.POST["CommentInput"]
        # Saving the information in the database
        documentosContrato = models.contratacion(
            NombreAspirante = aspirante,
            uploadedNotes = uploadedNotes,
            uploadedCV = uploadedCV,
            is_contratado = contratado,
            comentarios = Comentarios,
            
        )
        documentosContrato.save()
    context = {'registros': registros, 'asignacion':asignacion, 'users':users, 'hat':hat}
    return render(request, 'social/contrataciones.html',context)


def egg(request):
    context = {}
    return render(request, 'social/egg.html',context)

def generar_codigo_qr(request, user_id):
    try:
        id_user=user_id
        # Obtén el usuario correspondiente al user_id
        usuario = CredentialToken.objects.get(user_id=id_user)
        token_user= usuario.token
        print(usuario)
        # Construye la URL de la credencial del usuario cardex.tescacorporation.com
        
        url_credencial = reverse('credencial',args=[token_user])
        print(url_credencial)

        # Genera el código QR
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(request.build_absolute_uri(url_credencial))
        qr.make(fit=True)

        # Crea una imagen del código QR
        img = qr.make_image(fill_color="black", back_color="white")
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        image_data = buffer.getvalue()

        # Devuelve la imagen como respuesta HTTP
        return HttpResponse(image_data, content_type="image/png")
    except CredentialToken.DoesNotExist:
        # Manejar el caso en el que el usuario no exista
        return HttpResponse("Usuario no encontrado", status=404)



def pages(request):
    
    context = {}
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('social/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('social/errores/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('social/errores/page-500.html')
        return HttpResponse(html_template.render(context, request),)