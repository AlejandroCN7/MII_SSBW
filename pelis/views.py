from django.shortcuts import HttpResponse, render, HttpResponseRedirect
from mongoengine import *
from .models import Pelis
from django.urls import reverse
import re

import os


# Create your views here.

#-----------------------------------------------------------------------------------------------------------------------
def hola_mundo(request):

	salida = '''<html>
  			Hola mundo
		    </html>'''

	return HttpResponse(salida)

#-----------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------------
# Consultas con mongoengine
def pelisQueSale(request,actor):

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
def formulario(request):

	return render(request,"form.html")

def procesandoActor(request):

	actor = request.POST.get('actor')

	return HttpResponseRedirect(reverse('PelisQueSale',args=[actor]))

#-----------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------------
# Para sacar la vista de la película seleccionada desde la tabla
def mostrarPelicula(request,id):

	pelicula = Pelis.objects(id=id) # Como lo buscamos por id, nos va a salir una lista de un solo elemento
	context ={
		'pelicula': pelicula[0]
	}

	return render(request,"visualizador.html",context)
#-----------------------------------------------------------------------------------------------------------------------
