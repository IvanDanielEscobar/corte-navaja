from django.shortcuts import render
from .models import Corte, Reserva


def base(request):
    return render(request, 'corte/base.html')

def corte(request):
    cortes = Corte.objects.all()
    return render(request, 'corte/corte.html', {'cortes':cortes})

def bienvenida(request):
    return render(request, 'corte/bienvenida.html')

def corte_detail(request, id):
    corte = Corte.objects.get(id=id)
    return render(request, 'corte/corte_detail.html', {'corte': corte})

def reserva(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        telefono = request.POST['telefono']

    Reserva.objects.create(nombre=nombre, telefono=telefono)
    return render(request, 'corte/reserva.html', {'nombre': nombre, 'telefono': telefono})