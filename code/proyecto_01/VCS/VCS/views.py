from django.http.response import HttpResponse

def hello_world(response):
    return HttpResponse('Hola mundo')