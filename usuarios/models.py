from django.db import models

# Create your models here.
class usuario(models.Model):
    username = models.CharField(max_length=10)
    email = models.EmailField(unique=True, primary_key=True)
    contrasena = models.CharField(max_length=50)

    def __str__(self):
        return self.username