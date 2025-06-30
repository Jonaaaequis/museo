from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_museos, name='inicio_museos'),
    path('nuevo_museo/', views.nuevo_museo, name='nuevo_museo'),
    path('editar/<int:museo_id>/', views.editar_museo, name='editar_museo'),
    path('eliminar/<int:museo_id>/', views.eliminar_museo, name='eliminar_museo'),
]
