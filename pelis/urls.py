from django.urls import path
from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
	path('hola_mundo', views.hola_mundo),	# entrada str
	path('pelis que sale/<actor>', views.pelisQueSale, name ="PelisQueSale"), # Parte pymongo de tarea 5
	path('procesandoActor', views.procesandoActor),
	path('formulario', views.formulario, name= "formulario"),
	path('visualizador/<id>', views.mostrarPelicula, name= "visualizador"),
	path('crud', views.crudGeneral, name= "crudGeneral"),
	path('crud/<actor>', views.crud, name= "crud"),
	path('procesandoCrud', views.procesandoCrud),
	path('borrarPelicula/<id>', views.borrarPelicula),
	path('editarPelicula/<id>', views.editarPelicula),
	path('crearPelicula', views.crearPelicula),
	# Necesito estas tres por si modificamos algo de la tabla a partir de la búsqueda de un actor.
	path('crud/borrarPelicula/<id>', views.borrarPelicula),
	path('crud/editarPelicula/<id>', views.editarPelicula),
	path('crud/crearPelicula', views.crearPelicula),
	]