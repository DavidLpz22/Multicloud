from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarea

def lista_tareas(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion')
        Tarea.objects.create(titulo=titulo, descripcion=descripcion)
        return redirect('lista_tareas')
    
    tareas = Tarea.objects.all()
    return render(request, 'index.html', {'tareas': tareas})

def index(request):
    if request.method == 'POST':
        Tarea.objects.create(
            titulo=request.POST.get('titulo'),
            descripcion=request.POST.get('descripcion')
        )
        return redirect('index')
    
    tareas = Tarea.objects.all().order_by('-id')
    return render(request, 'index.html', {'tareas': tareas})

def eliminar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)
    tarea.delete()
    return redirect('index')

def completar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)
    tarea.completada = not tarea.completada # Cambia entre lista y pendiente
    tarea.save()
    return redirect('index')