from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReservaForm
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
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            nueva_reserva = form.save(commit=False)
            nueva_reserva.corte = corte
            nueva_reserva.save()
            return redirect('reserva_exitosa', id=nueva_reserva.id)
    else:
        form = ReservaForm()
    return render(request, 'corte/corte_detail.html', {'corte': corte, 'form': form})

def lista_reservas(request):
    reservas = Reserva.objects.all()
    return render(request, 'corte/lista_reservas.html', {'reservas': reservas})

def crear_reserva(request):
    form = ReservaForm(request.POST)
    if form.is_valid():
        nueva_reserva = form.save()
        return redirect('reserva', id=nueva_reserva.id)


def eliminar_reserva(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    reserva.delete()
    return redirect('lista_reservas')

def reserva_exitosa(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    return render(request, 'corte/reserva.html', {'reserva':reserva})