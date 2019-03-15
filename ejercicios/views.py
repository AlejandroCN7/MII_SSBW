from django.shortcuts import HttpResponse, render
import random
import re
import urllib.request
import re, string
import os

# Create your views here.


# Simplemente muestra un hola mundo en html como respuesta Http
def hola_mundo(request):

	salida = '''<html>
  			Hola mundo
		    </html>''' 

	return HttpResponse(salida)

#
def ejercicio1(request, lista):

	#Pasamos las cadenas separadas por comas en la url
	lista=lista.split(",")

	contador=0
	#Para cada cadena si se cumplen las condiciones sumamos uno al contador
	for cadena in lista:
		if(len(cadena)>1 and cadena[0]==cadena[len(cadena)-1]):
			contador +=1

	#En la salida html que irá incluida en el paquete http debemos de reflejar el contador calculado
	salida = '''<html>
  			Número de palabras aceptadas %s
		    </html>'''%(str(contador)) 

	return HttpResponse(salida)

def ejercicio2(request, lista):

	# Debemos dar la lista de números separadas por comas también
	lista=lista.split(",")

	lista = set(lista)
	salida = '''<html>
  			Números eliminando repetidos: %s
		    </html>'''%(str(lista)) 
	
	return HttpResponse(salida)

def ejercicio3(request, entrada):

	resultado=""
	if(len(entrada)<2):
		pass
	else:
		# Nos quedamos con las dos primeras y dos últimas letras de la palabra
		resultado += entrada[0:2] + entrada[len(entrada)-2:len(entrada)]

	salida = '''<html>
  			Dos primeras y dos últimas letras: %s
		    </html>'''%(resultado) 

	return HttpResponse(salida)

def ejercicio4(request, entrada):

	#Añadimos nada, ing o ly dependiendo de las condiciones descritas en el ejercicio y devolvemos la respuesta
	if(len(entrada)<3):
		pass
	elif(entrada[len(entrada)-3:len(entrada)]=="ing"):
		entrada += "ly"
	else:
		entrada += "ing"

	salida = '''<html>
  			Palabra transformada: %s
		    </html>'''%(entrada)

	return HttpResponse(salida)

def ejercicio5(request, entrada):

	#Con esto recogemos el archivo desde la misma carpeta en la que se encuentra views.py
	module_dir = os.path.dirname(__file__)  # get current directory
	file_path = os.path.join(module_dir, entrada)
	f = open(file_path,"r")
	mensaje = f.read()
	f.close()

	# Eliminamos los signos de puntuación
	mensaje = re.sub('[%s]' % re.escape(string.punctuation), ' ', mensaje)
	# Tambien debemos de eliminar los saltos de línea que puedan aparecer en el documento
	mensaje = re.sub('[%s]' % re.escape("[\\n]+"), ' ', mensaje)
	# Separamos cada palabra de tal forma que trabajamos con una lista
	mensaje = mensaje.split(" ")

	# Creamos el diccionario llamado "mimic" del ejercicio
	mimic = {}
	for i in range(0, len(mensaje)):
		palabra = mensaje[i]

		# Si es la última palabra y nunca antes ha aparecido debemos de crearle una lista vacía como definición
		if (i == len(mensaje) - 1):
			if (palabra not in mimic):
				mimic[palabra] = list()
		else:
			siguiente_palabra = mensaje[i + 1]
			# En caso de que la palabra ya estuviera en el diccionario añadimos la palabra que lo sigue en su lista de definición
			if palabra in mimic:
				mimic[palabra].append(siguiente_palabra)
			# Si es la primera vez que aparece debemos de crear la lista con la palabra siguiente de la que estamos analizando
			else:
				mimic[palabra] = [siguiente_palabra]

	# Ya tenemos el diccionario mimic creado
	#Nos quedamos con la primera palabra del mensaje
	palabra=mensaje[0]
	#Aquí iremos escribiendo el texto resultante
	texto=""
	#Añadimos la primera palabra
	texto+=palabra
	final = False
	while not final:
		# Eligimos una palabra aleatoria de su definición correspondiente en mimic
		palabra = random.choice(mimic[palabra])
		#Añadimos la palabra
		texto += " "
		texto += palabra
		# Si esa palabra no tiene clave en mimic o es una lista vacía finalizamos el proceso
		if (palabra not in mimic or mimic[palabra]==[]):
			final=True

	salida = '''<html>
  			%s
		    </html>'''%(texto)

	return HttpResponse(salida)

def ejemplo_plantilla(request):

	context={
		'año':2019,
		'lista': [
			{'nombre': 'Alex', 'número':2},
			{'nombre': 'Juan', 'número':256}
		]
	}

	return render(request, 'ejemplo.html', context)

def extract_pais(request,opcion):

	url = 'http://ep00.epimg.net/rss/tecnologia/portada.xml'

	respuesta = urllib.request.urlopen(url)
	contenidoWeb = respuesta.read()
	contenidoWeb = contenidoWeb.decode('utf-8')

	if(opcion == "titulos" or opcion == "todo"):

		textoTitulos = re.findall(r'<title><\!\[CDATA\[(.+?)\]\]><\/title>', contenidoWeb)
		titulos = []

		for content in textoTitulos:
			titulos.append({'titulo': content})

	if (opcion == "imagenes" or opcion == "todo"):

		urlImagenes = re.findall(r'<enclosure url="(.+?)"', contenidoWeb)
		imagenes = []

		for url in urlImagenes:
			imagenes.append({'imagen': url})


	context={}

	if(opcion=="todo"):

		context = {
			'opcion': 'todo',
			'titulos': titulos,
			'imagenes': imagenes
		}

	elif(opcion=="titulos"):

		context = {
			'opcion': 'titulos',
			'titulos': titulos,
		}

	elif(opcion=="imagenes"):

		context = {
			'opcion': 'imagenes',
			'imagenes': imagenes
		}

	else:
		context = {
			'opcion': 'nada',
		}


	#return HttpResponse(salida)
	return render(request, 'pais.html', context)
