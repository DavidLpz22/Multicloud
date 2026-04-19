from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # Aquí es donde realmente llamas a tu función index
    path('tareas/', views.lista_tareas, name='lista_tareas'), # Cambiamos la ruta para que no choquen
]