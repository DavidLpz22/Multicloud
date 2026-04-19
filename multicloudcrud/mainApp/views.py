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