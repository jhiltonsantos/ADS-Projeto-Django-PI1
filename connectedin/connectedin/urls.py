from django.contrib import admin
from django.contrib.auth import views as v
from django.urls import path
from perfis import views as perfil_v
from timeline import views as timeline_v
from usuarios.views import RegistrarUsuarioView
from timeline.views import TimelineView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', perfil_v.index, name='index'),
    path('perfil/<int:perfil_id>', perfil_v.display, name='exibir'),
    path('perfil/<int:perfil_id>/convidar',
         perfil_v.convidar, name='convidar'),
    path('convite/<int:convite_id>/aceitar', perfil_v.aceitar, name='aceitar'),
    path('registrar/', RegistrarUsuarioView.as_view(), name='registrar'),
    path('login/', v.LoginView.as_view(template_name="login.html"), name='login'),
    path('logout/', v.LogoutView.as_view(template_name="login.html"), name='logout'),
    path('timeline/', TimelineView.as_view(), name='timeline'),
    path('postar/', timeline_v.postar, name='postar')
]
