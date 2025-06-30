from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
# Create your views here.
from .models import Museo
#IMPORTANDO COMPONENTE DE MNSAJES DE CONFIRMACION
from django.contrib import messages

def inicio_museos(request):
    museos = Museo.objects.all()
    return render(request, 'inicio_museo.html', {'museos': museos})

def nuevo_museo(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        direccion = request.POST['direccion']
        ciudad = request.POST['ciudad']

        Museo.objects.create(nombre=nombre, direccion=direccion, ciudad=ciudad)
        messages.success(request,"Museo agregado correctamente") 
        return redirect('inicio_museos')
    
    return render(request, 'nuevo_museo.html')

def editar_museo(request, museo_id):
    museo = Museo.objects.get(id=museo_id)

    if request.method == 'POST':
        museo.nombre = request.POST['nombre']
        museo.direccion = request.POST['direccion']
        museo.ciudad = request.POST['ciudad']
        museo.save()
        messages.success(request,"Museo editado correctamente") 
        return redirect('inicio_museos')

    return render(request, 'editar_museo.html', {'museo': museo})

def eliminar_museo(request, museo_id):
    museo = Museo.objects.get(id=museo_id)
    museo.delete()
    messages.success(request,"Museo eliminado correctamente")   
    return redirect('inicio_museos')


