from django.urls import path
#mapeando a url

from . import views

urlpatterns = [
    path('', views.idex, name='index'),
]