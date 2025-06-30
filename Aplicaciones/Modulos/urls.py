from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_modulos, name='inicio_modulos'),
    path('nuevo_modulo/', views.nuevo_modulo, name='nuevo_modulo'),
    path('editar/<int:id>/', views.editar_modulo, name='editar_modulo'),
    path('eliminar/<int:id>/', views.eliminar_modulo, name='eliminar_modulo'),
]
