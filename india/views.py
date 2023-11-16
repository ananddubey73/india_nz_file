from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def virat(request):
    return HttpResponse('<h1>Virat has maked 50 century</h1>')

def shreyasiyer(request):
    return HttpResponse("<h1>He is score 100 in today match</h1>")

