from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.http import JsonResponse

from .models import Caballero

import facebook
import json

# Create your views here.

def index(request):
	caballeros = Caballero.objects.all()
	template = loader.get_template('orden_chatbot/index.html')
	return HttpResponse(template.render({'caballeros': caballeros},request))
def caballero(request):
	caballeros = Caballero.objects.all()
	arrCaballeros = []
	for caballero in caballeros:
		arrCaballeros.append({"nombre":caballero.nombre, "puto":caballero.puto})
	return JsonResponse(arrCaballeros, safe=False)
def loginFB(request):
	data = json.loads(request.body.decode('utf-8'))
	print(data)
	graph = facebook.GraphAPI(access_token=data["authResponse"]["accessToken"], version="3.1")
	permissions = graph.get_permissions(user_id=data["authResponse"]["userID"])
	print(permissions)
	return HttpResponse(str(permissions))
