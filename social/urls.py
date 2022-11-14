from django.conf.urls import url
from django.urls import path, include
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('inicio/', views.inicio, name='inicio'),
    path('', views.feed, name='feed'),
    path('profile/', views.profile, name='profile'),
    url(r'^information/$', views.information, name='information'),
    url(r'^hats/$', views.hats, name='hats'),
    url(r'^rewards/$', views.rewards, name='rewards'),
    #Perfil Medico
    url(r'^perfilmedico/$', views.perfilmedico, name='perfilmedico'),
    path('perfilmedico/<str:username>/', views.perfilmedicodentro, name='perfilmedico'),
    #Perfil Legal
    url(r'^perfillegal/$', views.perfillegal, name='perfillegal'),

    url(r'^datosmedicos/$', views.datosmedicos, name='datosmedicos'),
    path('datosmedicos/<str:username>/', views.datosmedicos, name='datosmedicos'),

    url(r'^verdatosmedicos/$', views.verdatosmedicos, name='verdatosmedicos'),
    path('verdatosmedicos/<str:username>/', views.verdatosmedicos, name='verdatosmedicos'),

    url(r'^regasis/$', views.regasis, name='regasis'),
    url(r'^asistencia/$', views.asistencia, name='asistencia'),
    
    #Perfil Psicologico
    url(r'^perfilpsico/$', views.perfilpsico, name='perfilpsico'),
    
    #Subir Archivos Psicologicos
    url(r'^uploadpsico/$', views.uploadpsico, name='uploadpsico'),
    path(r'^uploadpsico/<str:username>/', views.uploadpsico, name='uploadpsico'),

    #perfil Actas Kaisen
    url(r'^perfilKaisen/$', views.perfilkaisen, name='perfilKaisen'),
    path('perfilkaisen/<str:username>/', views.perfilkaisenusuario, name='perfilKaisen'),

    #Datos kaisen
    url(r'^kaisenfiles/$', views.kaisenfiles, name='kaisenfiles'),
    path(r'^kaisenfiles/<str:username>/', views.kaisenfiles, name='kaisenfiles'),
    #subir Actas Kaisen
    url(r'^uploadkaisen/$', views.uploadkaisen, name='uploadkaisen'),
    path(r'^uploadkaisen/<str:username>/', views.uploadkaisen, name='uploadkaisen'),

    #Subir Archivos Medicos
    url(r'^uploadmedic/$', views.uploadmedic, name='uploadmedic'),
    path(r'^uploadmedic/<str:username>/', views.uploadmedic, name='uploadmedic'),
    
    #Subir Archivos Justificantes
    url(r'^uploadmedicjust/$', views.uploadmedicjust, name='uploadmedicjust'),
    path(r'^uploadmedicjust/<str:username>/', views.uploadmedicjust, name='uploadmedicjust'),
    
    #Subir Archivos Legales
    url(r'^uploadlegal/$', views.uploadlegal, name='uploadlegal'),
    path(r'^uploadlegal/<str:username>/', views.uploadlegal, name='uploadlegal'),
    url(r'^subirdocumentacion/$', views.subirdocumentacion, name='subirdocumentacion'),
    
    #Datos Psicologicos
    url(r'^files/$', views.files, name='files'),
    path(r'^files/<str:username>/', views.files, name='files'),
    
    #Datos medicos
    url(r'^medicfiles/$', views.medicfiles, name='medicfiles'),
    path(r'^medicfiles/<str:username>/', views.medicfiles, name='medicfiles'),
    #Datos Legales
    url(r'^legalfiles/$', views.legalfiles, name='legalfiles'),
    path(r'^legalfiles/<str:username>/', views.legalfiles, name='legalfiles'),

    path('legalDocumentos/', views.legalDocumentos, name='legalDocumentos'),
    path('legalDocumentos/<str:username>/', views.legalDocumentos, name='legalDocumentos'),

    path('inclusiondocumentos/', views.inclusiondocumentos, name='inclusiondocumentos'),
    path('inclusiondocumentos/<str:username>/', views.inclusiondocumentos, name='inclusiondocumentos'),
    url(r'^subirinclusion/$', views.subirinclusion, name='subirinclusion'),
    
    #Justificantes Medicos
    url(r'^justifyfiles/$', views.justifyfiles, name='justifyfiles'),
    path(r'^justifyfiles/<str:username>/', views.justifyfiles, name='justifyfiles'),

    # cards QR
    path('credencial/', views.credencial, name='credencial'),
    path('credencial/<str:id>/', views.credencial, name='credencial'),
    
    
    url(r'^viewfiles/$', views.viewfiles, name='viewfiles'),
    path(r'^viewfiles/<str:username>/', views.viewfiles, name='viewfiles'),
    url(r'^asignarhat/$', views.asignarhat, name='asignarhat'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='social/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='social/logout.html'), name='logout'),
    path('post_in_or_post_out/', views.post, name='post'),
    path('follow/<str:username>/', views.follow, name='follow'),
    path('unfollow/<str:username>/', views.unfollow, name='unfollow'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'Cardex'
