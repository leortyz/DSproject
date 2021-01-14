from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.renderers import TemplateHTMLRenderer

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def welcome(request):
    return render(request, 'template.html')

def about_us(request):
    return render(request, 'test.html')

class UploadImage(APIView):
    def post(self, request, format=None):
        #Agregar a la tabla imagen, usar el modelo 
        print("")
