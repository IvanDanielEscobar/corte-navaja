from django.urls import path

from . import views

urlpatterns = [
    path('', views.bienvenida, name='bienvenida'),
    path('seleccion-corte/', views.corte, name='corte'),
    path('corte-detail/<int:id>/', views.corte_detail, name='detail'),
    path('reserva/', views.reserva, name='reserva'),
]