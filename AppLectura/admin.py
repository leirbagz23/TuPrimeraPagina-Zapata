from django.contrib import admin

# Register your models here.
from AppLectura.models import Leidos, Por_Leer, Leyendo
admin.site.register(Leidos)
admin.site.register(Por_Leer)
admin.site.register(Leyendo)
