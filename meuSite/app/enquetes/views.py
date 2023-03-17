from django.shortcuts import render

# Create your views here.

#comando para criar primeiro view

from django.http import HttpResponse

def index(request):
    return HttpResponse("Olá mundo. você está no índice enquetes.")