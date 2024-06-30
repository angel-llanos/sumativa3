from django.forms import ModelForm
from .models import usuario

class UsuarioForm(ModelForm):
    class Meta:
        model = usuario
        fields = "__all__"