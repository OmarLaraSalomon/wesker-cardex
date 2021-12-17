from django.conf.urls import url
from django.urls import path
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path('', views.feed, name='feed'),
    path('profile/', views.profile, name='profile'),
    url(r'^information/$', views.information, name='information'),
    url(r'^hats/$', views.hats, name='hats'),
    url(r'^regasis/$', views.regasis, name='regasis'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='social/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='social/logout.html'), name='logout'),
    path('post_in_or_post_out/', views.post, name='post'),
    path('follow/<str:username>/', views.follow, name='follow'),
    path('unfollow/<str:username>/', views.unfollow, name='unfollow'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'Cardex'
