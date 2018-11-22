from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Caballero

# Create your views here.

def index(request):
	caballeros = Caballero.objects.all()
	template = loader.get_template('orden_chatbot/index.html')
	return HttpResponse(template.render({'caballeros': caballeros},request))
