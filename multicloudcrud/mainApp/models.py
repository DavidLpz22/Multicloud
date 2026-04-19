from django.db import migrations, models


class Tarea(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    completada = models.BooleanField(default=False) # Para marcar como lista


    def __str__(self):
        return self.titulo
    


