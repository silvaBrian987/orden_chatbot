from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie

from .models import Caballero
from .models import Configuracion

import facebook
import json

# Create your views here.
MOCK_CLIENT_ID = "2379676135438619"

#@ensure_csrf_cookie
def index(request):
	caballeros = Caballero.objects.all()
	template = loader.get_template('orden_chatbot/index.html')
	return HttpResponse(template.render({'caballeros': caballeros}, request))
def caballero(request):
	caballeros = Caballero.objects.all()
	arrCaballeros = []
	for caballero in caballeros:
		arrCaballeros.append({"nombre":caballero.nombre, "puto":caballero.puto})
	return JsonResponse(arrCaballeros, safe=False)
def loginFB(request):
	strJson = request.body.decode('utf-8')
	if len(strJson) > 0:
		data = json.loads(strJson)
		print(data)
	#graph = facebook.GraphAPI(access_token=data["authResponse"]["accessToken"], version="3.1")
	app_id = Configuracion.objects.get(clave='facebook.app.id')
	app_secret = Configuracion.objects.get(clave='facebook.app.secret')
	#print(app_id)
	graph = facebook.GraphAPI(access_token=app_id.valor + "|" + app_secret.valor, version="3.1")
	#permissions = graph.get_permissions(user_id=data["authResponse"]["userID"])
	#permissions = graph.get_permissions(user_id="")
	accounts = graph.get_object(id="me/accounts")
	print(accounts)
	return HttpResponse(str(accounts))
