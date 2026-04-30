from django.urls import path

from . import views

urlpatterns = [
    path('', views.bienvenida, name='bienvenida'),
    path('seleccion-corte/', views.corte, name='corte'),
    path('corte-detail/<int:id>/', views.corte_detail, name='detail'),
    path('reservas/', views.lista_reservas, name='lista_reservas'),
    path('reservas/eliminar/<int:id>/', views.eliminar_reserva, name='eliminar_reserva'),
    path('reserva/<int:id>/', views.reserva_exitosa, name='reserva_exitosa')
]