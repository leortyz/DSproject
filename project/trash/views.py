from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from django.core.files.storage import FileSystemStorage
from .models import *




def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def about_us(request):
    return render(request, 'test.html')

class Home(APIView):
    def get(self, request, format=None):   
        return render(request, 'template.html')

    def post(self, request, format=None):
        imagen= request.FILES['file']
        if imagen:
            fileimg= FileSystemStorage()
            saved= fileimg.save(imagen.name, imagen)
            ruta= fileimg.url(saved) 
            context={
                'img':imagen.name,
                'size':imagen.size,
                'type': str(imagen.content_type),
                'error': '',
                'class': '',
            }
            
            print(Trash.objects.count())
            try:
                #realizar el analisis
                #resultado agregar a trash_created
                #context['class']="Cambiar"
                trash_created = Trash.objects.create(trash_type="Plastic")
                Image.objects.create(trash=trash_created, name=imagen.name, img=str(ruta))
            except:
                context['error']="No se pudo analizar correctamente la imagen"
                return render(request, 'result.html', context)
            else:
                return render(request, 'result.html', context)
        else:
            return render(request, 'result.html')
