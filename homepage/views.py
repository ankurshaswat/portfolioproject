from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    #return HttpResponse("Hello, world. You're at the homepage index.")
    #template = loader.get_template('homepage/index.html')
    context = {
    }
    return render(request, 'homepage/index.html', context)

