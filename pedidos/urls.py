from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pedido/', views.cargando_un_pedido, name='pedido'),
    path('soloform/', views.soloform, name='soloform'),
]