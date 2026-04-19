from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.get_id()),
    path('', include('mainApp.urls')), # <--- ASEGÚRATE DE QUE ESTO EXISTE
]
