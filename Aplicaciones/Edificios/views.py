from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Edificio

def inicio_edificios(request):
    edificios = Edificio.objects.all()
    return render(request, 'inicio_edificio.html', {'edificios': edificios})

def nuevo_edificio(request):
    if request.method == 'POST':
        edificio = request.POST.get('edificio')
        escala = request.POST.get('escala')
        materiales = request.POST.get('materiales')
        construccion = request.POST.get('construccion')
        proposito = request.POST.get('proposito')
        ubicacion = request.POST.get('ubicacion')
        nivel = request.POST.get('nivel')
        
        Edificio.objects.create(
            edificio=edificio,
            escala=escala,
            materiales=materiales,
            construccion=construccion,
            proposito=proposito,
            ubicacion=ubicacion,
            nivel=nivel
        )
        messages.success(request, "Edificio agregado correctamente")
        return redirect('inicio_edificios')
    
    return render(request, 'nuevo_edificio.html')

def editar_edificio(request, id):
    edificio = get_object_or_404(Edificio, id=id)
    
    if request.method == 'POST':
        edificio.edificio = request.POST.get('edificio')
        edificio.escala = request.POST.get('escala')
        edificio.materiales = request.POST.get('materiales')
        edificio.construccion = request.POST.get('construccion')
        edificio.proposito = request.POST.get('proposito')
        edificio.ubicacion = request.POST.get('ubicacion')
        edificio.nivel = request.POST.get('nivel')
        edificio.save()
        
        messages.success(request, "Edificio actualizado correctamente")
        return redirect('inicio_edificios')
    
    return render(request, 'editar_edificio.html', {'edificio': edificio})

def eliminar_edificio(request, id):
    edificio = get_object_or_404(Edificio, id=id)
    edificio.delete()
    messages.success(request, "Edificio eliminado correctamente")
    return redirect('inicio_edificios')
