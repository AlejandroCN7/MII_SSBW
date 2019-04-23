from django.shortcuts import HttpResponse, render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from mongoengine import *
from .models import Pelis
from django.urls import reverse
import re
import logging


logger = logging.getLogger(__name__)

# Create your views here.

#-----------------------------------------------------------------------------------------------------------------------
def hola_mundo(request):

	logger.debug("ACCEDIENDO A RECURSO DE HOLA MUNDO")

	salida = '''<html>
  			Hola mundo
		    </html>'''

	return HttpResponse(salida)

#-----------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------------
# Consultas con mongoengine
def pelisQueSale(request,actor):

	logger.debug("BUSCANDO ACTOR %S EN LA BASE DE DATOS", actor)

	regex = re.compile(actor)
	peliculas = Pelis.objects(actors=regex)
	context = {
		'lista': peliculas,
		'actor': True,
		'resultados': peliculas.count(),
	}

	return render(request,"tabla.html",context)
#-----------------------------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------------------------
#Formulario y su posterior procesamiento desde backend
@login_required
def formulario(request):

	logger.debug("ABRIENDO FORMULARIO")

	return render(request,"form.html")

def procesandoActor(request):

	logger.debug("PROCESANDO ACTOR DEL POST")

	actor = request.POST.get('actor')

	return HttpResponseRedirect(reverse('PelisQueSale',args=[actor]))

#-----------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------------
# Para sacar la vista de la película seleccionada desde la tabla
@login_required
def mostrarPelicula(request,id):

	logger.debug("OBTENIENDO INFORMACIÓN DE LA PELÍCULA %s", id)

	pelicula = Pelis.objects(id=id) # Como lo buscamos por id, nos va a salir una lista de un solo elemento
	context ={
		'pelicula': pelicula[0]
	}

	return render(request,"visualizador.html",context)
#-----------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------------
def crudGeneral(request):

	logger.debug("ABRIENDO CRUD CON TODAS LAS PELÍCULAS")

	peliculas = Pelis.objects().all().order_by('title')
	context = {
		'lista' : peliculas,
		'general': True,
	}

	return render(request,"crud.html",context)

# Consultas con mongoengine
@login_required
def crud(request,actor):
	logger.debug("CRUD CON PELÍCULAS EN LAS QUE SALE %s", actor)

	regex = re.compile(actor)
	peliculas = Pelis.objects(actors=regex).order_by('title')
	context = {
		'lista': peliculas,
		'resultados': peliculas.count(),
	}

	return render(request,"crud.html",context)

def procesandoCrud(request):

	actor = request.POST.get('actor')

	return HttpResponseRedirect(reverse('crud',args=[actor]))
#-----------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------------
# Borrar películas por su id con mongoengine

@login_required
def borrarPelicula(request,id):
	logger.debug("BORRANDO PELÍCULA %s", id)

	pelicula = Pelis.objects(id=id)

	if(pelicula.count()==1):
		pelicula.delete()

	return HttpResponseRedirect(reverse('crudGeneral'))
#-----------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------------
# Editar Películas por su id con mongoengine

@login_required
def editarPelicula(request,id):
	logger.debug("EDITANDO PELÍCULA %s", id)

	pelicula = Pelis.objects(id=id)
	# Doy la opción de que los campos que se dejen en blanco no se actualicen (ninguno de los campos a actualizar son
	# obligatorios). Por ello tengo que ir campo por campo comprobando que no estén vación en lugar de hacerlo todo
	# junto en una misma línea

	# Entonces, el usuario puede cambiar solo datos concretos.
	if(request.method == "POST"):
		parametros = request.POST

		if(parametros.get('titulo')!=''):
			pelicula.update_one(title=parametros.get('titulo'))

		if (parametros.get('año') != ''):
			pelicula.update_one(year=parametros.get('año'))

		if (parametros.get('director') != ''):
			pelicula.update_one(director=parametros.get('director'))

		if (parametros.get('reparto') != ''):
			# Para poder mantener las listas internamente
			reparto = parametros.get('reparto').split(", ")
			pelicula.update_one(actors=reparto)

		if (parametros.get('puntuacion') != ''):
			pelicula.update_one(imdb__rating=parametros.get('puntuacion'))

		if (parametros.get('duracion') != ''):
			pelicula.update_one(runtime=parametros.get('duracion'))


	return HttpResponseRedirect(reverse('crudGeneral'))
#-----------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------------
@login_required
def crearPelicula(request):

	# En este caso tenemos establecido en el front-end que todos los campos son obligatorios, por lo que no tenemos que
	# preocuparnos por supuestos campos vacíos.

	logger.debug("CREANDO PELÍCULA NUEVA")

	if(request.method == "POST"):

		parametros = request.POST

		# Nos ocurre lo mismo que al editar películas
		reparto = parametros['reparto'].split(", ")

		pelicula = Pelis(title=parametros['titulo'],
						 year= parametros['año'],
						 director=parametros['director'],
						 actors = reparto,
						 imdb = { 'rating' : parametros['puntuacion']},
						 runtime = parametros['duracion'])

		pelicula.save()

	return HttpResponseRedirect(reverse('crudGeneral'))

#-----------------------------------------------------------------------------------------------------------------------