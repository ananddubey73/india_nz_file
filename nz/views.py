from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def kanewillamson(request):
    return HttpResponse('<h1>It will score 50 in semifinal match</h1>')

def darylmitchell(request):
    return HttpResponse('<h1>Mitchell will score 100</h1>')