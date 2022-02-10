from django.http.response import HttpResponse
from datetime import datetime

def hello_world(response):
    return HttpResponse('Hola mundo')

def hola(response):
    fecha_actual = datetime.now().strftime('%b %th, %Y - %H:%M hrs')
    return HttpResponse( 'El tiempo del servidor es {}'.format(fecha_actual) )

def obtener_numeros(response):
    numeros = response.Get['numeros']
    return HttpResponse( str(numeros) )

def obtener_numeros_ordenados(response):
    numeros = [ int(i) for i in response.GET['numeros'].split(',') ]
    return HttpResponse( '' )