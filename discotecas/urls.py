from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_discotecas, name='listar_discotecas'),
    path('crear/', views.crear_discoteca, name='crear_discoteca'),
    path('editar/<int:id>/', views.editar_discoteca, name='editar_discoteca'),
    path('eliminar/<int:id>/', views.eliminar_discoteca, name='eliminar_discoteca'),
]
