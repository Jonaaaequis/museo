from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import ModuloInteractivo
#IMPORTANDO COMPONENTE DE MNSAJES DE CONFIRMACION
from django.contrib import messages

from Aplicaciones.Museos.models import Museo
from Aplicaciones.Disenadores.models import DisenadorUX


def inicio_modulos(request):
    modulos = ModuloInteractivo.objects.select_related('museo', 'disenador').all()
    return render(request, 'inicio_modulo.html', {'modulos': modulos})

def nuevo_modulo(request):
    museos = Museo.objects.all()
    disenadores = DisenadorUX.objects.all()

    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion')
        museo_id = request.POST.get('museo')
        disenador_id = request.POST.get('disenador')

        museo = Museo.objects.get(id=museo_id)
        disenador = DisenadorUX.objects.get(id=disenador_id)

        ModuloInteractivo.objects.create(
            titulo=titulo,
            descripcion=descripcion,
            museo=museo,
            disenador=disenador
        )
        messages.success(request,"Modulo agregado correctamente") 
        return redirect('inicio_modulos')

    return render(request, 'nuevo_modulo.html', {
        'museos': museos,
        'disenadores': disenadores
    })

def editar_modulo(request, id):
    modulo = ModuloInteractivo.objects.get(id=id)
    museos = Museo.objects.all()
    disenadores = DisenadorUX.objects.all()

    if request.method == 'POST':
        modulo.titulo = request.POST.get('titulo')
        modulo.descripcion = request.POST.get('descripcion')
        modulo.museo = Museo.objects.get(id=request.POST.get('museo'))
        modulo.disenador = DisenadorUX.objects.get(id=request.POST.get('disenador'))
        modulo.save()
        messages.success(request,"Modulo aditado correctamente")
        return redirect('inicio_modulos')

    return render(request, 'editar_modulo.html', {
        'modulo': modulo,
        'museos': museos,
        'disenadores': disenadores
    })

def eliminar_modulo(request, id):
    modulo = ModuloInteractivo.objects.get(id=id)
    modulo.delete()
    messages.success(request,"Modulo eliminado correctamente") 
    return redirect('inicio_modulos')