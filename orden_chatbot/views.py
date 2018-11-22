from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
	return HttpResponse("Puto el que lee")
def basic_json(request):
	return HttpResponse({"name" : "puto", "type" : "dicc"})
def testingHTML(request):
	return HttpResponse("""
<html>
<head>
<title>THIS IS A TEST FROM LA ORDEN DE LA MESITA</title>
</head>
<body>
<h1>NOS HICIERON UN FAFNFIC</h1>
</body>
</html>
""")
