from django.shortcuts import HttpResponse, render
from mongoengine import *

import os


# Create your views here.

#-----------------------------------------------------------------------------------------------------------------------
def hola_mundo(request):

	salida = '''<html>
  			Hola mundo
		    </html>'''

	return HttpResponse(salida)

#-----------------------------------------------------------------------------------------------------------------------

