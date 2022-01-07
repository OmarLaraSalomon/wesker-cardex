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
    url(r'^regasis/$', views.regasis, name='regasis'),
    
    url(r'^perfilpsico/$', views.perfilpsico, name='perfilpsico'),
    
    url(r'^uploadpsico/$', views.uploadpsico, name='uploadpsico'),
    path(r'^uploadpsico/<str:username>/', views.uploadpsico, name='uploadpsico'),
    
    url(r'^files/$', views.files, name='files'),
    path(r'^files/<str:username>/', views.files, name='files'),
    
    url(r'^viewfiles/$', views.viewfiles, name='viewfiles'),
    path(r'^viewfiles/<str:username>/', views.viewfiles, name='viewfiles'),
    
    path('profile/<str:username>/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='social/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='social/logout.html'), name='logout'),
    path('post_in_or_post_out/', views.post, name='post'),
    path('follow/<str:username>/', views.follow, name='follow'),
    path('unfollow/<str:username>/', views.unfollow, name='unfollow'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'Cardex'
