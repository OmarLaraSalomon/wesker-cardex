from django.conf.urls import url
from django.urls import path,re_path,include
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.views import  PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('inicio/', views.inicio, name='inicio'),
    path('', views.feed, name='feed'),
    path('profile/', views.profile, name='profile'),
    path('constancia/<str:username>/', views.constancia, name='constancia'),
    path('renuncia/<str:username>/', views.renuncia, name='renuncia'),
    path('finiquito/<str:username>/', views.finiquito, name='finiquito'),
    #Perfil Legal
    path('perfillegal/<int:id>/', views.perfillegal, name='perfillegal'),
    
    url(r'^information/$', views.information, name='information'),
    url(r'^hats/$', views.hats, name='hats'),
    url(r'^cartas/$', views.cartas, name='cartas'),
    url(r'^rewards/$', views.rewards, name='rewards'),
    #Perfil Medico
    url(r'^perfilmedico/$', views.perfilmedico, name='perfilmedico'),
    path('perfilmedico/<str:username>/', views.perfilmedicodentro, name='perfilmedico'),
    

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
    
    #contrataciones
    path('contrataciones/', views.contrataciones, name='contrataciones'),
    url(r'^subircontratacion/$', views.subircontratacion, name='subircontratacion'),

    path('qr/<int:user_id>/', views.generar_codigo_qr, name='generar_codigo_qr'),
    # cards QR
    path('credencial/', views.credencial, name='credencial'),
    path('credencial/<str:tokenid>/', views.credencial, name='credencial'),
    
    #credenciales fisicas
    url('credencial_fisica/',views.credencial_fisica, name='credencial_fisica'),
    path("ver/<int:id>",views.ver, name="ver"),
    
    
    url(r'^viewfiles/$', views.viewfiles, name='viewfiles'),
    path(r'^viewfiles/<str:username>/', views.viewfiles, name='viewfiles'),
    url(r'^asignarhat/$', views.asignarhat, name='asignarhat'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('asignaregreso/<int:user_id>/', views.asignaregreso, name='asignaregreso'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='social/login.html'), name='login'),

    path('reset/password_reset', PasswordResetView.as_view(template_name='social/registration/password_reset_form.html', email_template_name="social/registration/password_reset_email.html"), name = 'password_reset'),

    path('reset/password_reset_done', PasswordResetDoneView.as_view(template_name='social/registration/password_reset_done.html'), name = 'password_reset_done'),

     re_path(r'^reset/(?P<uidb64>[0-9A-za-z_\-]+)/(?P<token>.+)/$', PasswordResetConfirmView.as_view(template_name='social/registration/password_reset_confirm.html'), name = 'password_reset_confirm'),

    path('reset/done',PasswordResetCompleteView.as_view(template_name='social/registration/password_reset_complete.html') , name = 'password_reset_complete'),
    
    path('logout/', LogoutView.as_view(template_name='social/logout.html'), name='logout'),
    path('post_in_or_post_out/', views.post, name='post'),
    path('follow/<str:username>/', views.follow, name='follow'),
    path('unfollow/<str:username>/', views.unfollow, name='unfollow'),
    path('egg', views.egg, name='egg'),
    re_path(r'^.*\.*', views.pages, name='pages'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'Cardex'
