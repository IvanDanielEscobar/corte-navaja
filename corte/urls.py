from django.urls import path

from . import views

urlpatterns = [
    path('', views.bienvenida, name='bienvenida'),
    path('seleccion-corte/', views.corte, name='corte'),
    path('corte-detail/', views.corte_detail, name='detail'),
]