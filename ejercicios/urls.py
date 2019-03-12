from django.urls import path

from . import views

urlpatterns = [
	path('hola_mundo', views.hola_mundo),	# entrada str
	path('ejercicio1/<lista>', views.ejercicio1), # entrada str, dada una lista de strings te dice el número de palabras con tamaño mayor a 2 y que empizan y acaban por la misma letra
	path('ejercicio2/<lista>', views.ejercicio2), # entrada str, dada una lista de números, te elimina aquellos valores que están repetidos
	path('ejercicio3/<entrada>', views.ejercicio3), # entrada str, dado un string, te devuelve una palabra con las 2 primeras y ultimas letras del string o cadena vacío si tiene un número de letras inferior a 2
	path('ejercicio4/<entrada>', views.ejercicio4), # entrada str, añade ing a la entrada, si ya acaba en ing añade ly, si el tamaño es menor que 3 la deja como está
	path('ejercicio5/<entrada>', views.ejercicio5), # entrada str, ejercicio 5
	path('extract_names/<filename>', views.extract_names),
	]
