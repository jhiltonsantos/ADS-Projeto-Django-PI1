from django.contrib import admin
from django.contrib.auth import views as v
from django.urls import path
from perfis import views
from usuarios.views import RegistrarUsuarioView
from timeline.views import TimelineView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('perfil/<int:perfil_id>', views.display, name = 'exibir'),
    path('perfil/<int:perfil_id>/convidar', views.convidar, name='convidar'),
    path('convite/<int:convite_id>/aceitar', views.aceitar, name='aceitar'),
    path('registrar/', RegistrarUsuarioView.as_view(), name='registrar'),
    path('login/', v.LoginView.as_view(template_name="login.html"), name='login'),
    path('logout/', v.LogoutView.as_view(template_name="login.html"), name='logout'),
    path('postar/', views.postar, name='postar')
]
