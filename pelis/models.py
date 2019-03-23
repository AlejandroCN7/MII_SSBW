from django.db import models
from mongoengine import *
# Create your models here.

connect('movies', host='mongo')

#Con estos modelos podemos consultar, añadir, eliminar cosas en la base de datos por medio de estas instancias
# Lo cual es más cómodo bajo el punto de vista del programador (Tenemos la info en instancias)
class Pelis(Document):
    title = StringField(required=True)
    year = IntField(min_value=1900)
    rated = StringField()
    runtime = IntField()
    countries = ListField(StringField())
    genres = ListField(StringField())
    director = StringField()
    writers = StringField()
    actors = ListField(StringField())
    plot = StringField()
    poster = URLField()
    imdb = DictField()
    awards = DictField()
    type = StringField()
    tomato = DictField()
    metacritic = IntField()
