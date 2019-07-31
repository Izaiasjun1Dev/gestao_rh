from django.db import models

class Registro_Hora_Extra(models.Model):
    motivo = models.CharField(max_length=100)

    def __str__(self):
        return self.motivo