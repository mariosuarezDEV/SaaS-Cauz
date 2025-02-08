from django.contrib import admin

# Register your models here.
from .models import ModelIntegrantes, ModelPresentaciones

class PresentacionesAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_agrupacion', 'presentacion_grupo',)
    search_fields = ('nombre_agrupacion',)
    date_hierarchy = 'marca_temporal'

admin.site.register(ModelPresentaciones, PresentacionesAdmin)

admin.site.register(ModelIntegrantes)