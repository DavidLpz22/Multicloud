from django.shortcuts import render, redirect
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
        # Guardar la tarea
        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion')
        Tarea.objects.create(titulo=titulo, descripcion=descripcion)
        return redirect('index') # Recarga la página para mostrar la nueva tarea

    # Obtener todas las tareas para mostrarlas
    tareas = Tarea.objects.all().order_by('-id')
    return render(request, 'index.html', {'tareas': tareas})