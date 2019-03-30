from django.urls import path

from . import views

urlpatterns = [
	path('hola_mundo', views.hola_mundo),	# entrada str
	path('pelis que sale/<actor>', views.pelisQueSale, name ="PelisQueSale"), # Parte pymongo de tarea 5
	path('procesandoActor', views.procesandoActor),
	path('formulario', views.formulario, name= "formulario"),
	path('visualizador/<id>', views.mostrarPelicula, name= "visualizador"),
	]