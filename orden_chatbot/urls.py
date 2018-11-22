from django.urls import path

from . import views

urlpatterns=[path('', views.index, name='index'),
path('basic_json/', views.basic_json, name='basic_json'),
path('testingHTML/', views.testingHTML, name='testingHTML'),
]
