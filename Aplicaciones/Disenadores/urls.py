from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_disenadores, name='inicio_disenadores'),
    path('nuevo_disenador/', views.nuevo_disenador, name='nuevo_disenador'),
    path('editar_disenador/<int:id>/', views.editar_disenador, name='editar_disenador'),
    path('eliminar_disenador/<int:id>/', views.eliminar_disenador, name='eliminar_disenador'),
]
