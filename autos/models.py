from django.db import models

# Create your models here.

class Auto(models.Model):
    id_auto = models.AutoField(db_column="id_autos", primary_key=True)
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=50)
    anio = models.IntegerField(null=False)
    descripcion = models.CharField(max_length= 150)
    precio = models.IntegerField(null=False)
    imagen = models.CharField(max_length=250, null=True)

    def __str__(self):
        return str(self.marca) + " " + str(self.modelo) + " " + str(self.anio)