from django.contrib import admin
from .models import Corte, Reserva

@admin.register(Corte)
class CorteAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'precio')
    search_fields = ('name',)
    list_filter = ('precio',)

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'telefono', 'corte')
    search_fields = ('nombre',)
    list_filter = ('corte',)