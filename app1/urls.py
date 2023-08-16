from django.urls import path
from . import views


urlpatterns = [
    path('index/',views.index , name='index'),
    path('crearveterinario/', views.crearveterinario, name='crearveterinario'),
    path('crearcliente/', views.crearcliente,name='crearcliente'),
    path('crearmascota/',views.crearmascota,name='crearmascota'),
    path('buscarmascota/',views.buscarmascota,name='buscarmascota'),
]