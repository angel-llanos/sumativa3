from django.contrib import admin
from .models import login
from .models import register

# Register your models here.
admin.site.register(login)
admin.site.register(register)