from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
# Create your views here.
from .models import DisenadorUX
#IMPORTANDO COMPONENTE DE MNSAJES DE CONFIRMACION
from django.contrib import messages

def inicio_disenadores(request):
    disenadores = DisenadorUX.objects.all()
    return render(request, 'inicio_disenador.html', {'disenadores': disenadores})

def nuevo_disenador(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        correo = request.POST.get('correo')
        experiencia = request.POST.get('experiencia')
        DisenadorUX.objects.create(nombre=nombre, correo=correo, experiencia=experiencia)
        messages.success(request,"Diseñador agregado correctamente") 
        return redirect('inicio_disenadores') 
    return render(request, 'nuevo_disenador.html')

def editar_disenador(request, id):
    disenador = get_object_or_404(DisenadorUX, id=id)
    if request.method == 'POST':
        disenador.nombre = request.POST.get('nombre')
        disenador.correo = request.POST.get('correo')
        disenador.experiencia = request.POST.get('experiencia')
        disenador.save()
        # MENSAJE DE CONFIRMACION
        messages.success(request,"Diseñador editado correctamente")  
        return redirect('inicio_disenadores')
    return render(request, 'editar_disenador.html', {'disenador': disenador})

def eliminar_disenador(request, id):
    disenador = get_object_or_404(DisenadorUX, id=id)
    disenador.delete()
    messages.success(request,"Diseñador eliminado correctamente")  
    return redirect('inicio_disenadores')