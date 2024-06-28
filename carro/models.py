from django.db import models

# Create your models here.

class carro (models.Model):
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=50)
    precio = models.IntegerField(null=False)
    
    def __str__(self):
        return str(self.marca) + " " + str(self.modelo) + " " + str(self.precio)
    