from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_edificios, name='inicio_edificios'),
    path('nuevo_edificio/', views.nuevo_edificio, name='nuevo_edificio'),
    path('editar_edificio/<int:id>/', views.editar_edificio, name='editar_edificio'),
    path('eliminar_edificio/<int:id>/', views.eliminar_edificio, name='eliminar_edificio'),
]
