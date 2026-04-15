from django.shortcuts import render
from .models import Corte


def base(request):
    return render(request, 'corte/base.html')


def corte(request):
    cortes = Corte.objects.all()
    return render(request, 'corte/corte.html', {'cortes':cortes})


def bienvenida(request):
    return render(request, 'corte/bienvenida.html')

def corte_detail(request):
    return render(request, 'corte/corte_detail.html')
