
from nz.views import *
from django.urls import path

app_name='kenwill'
urlpatterns=[
     path('kanewillamson',kanewillamson,name='kanewillamson'),
     path('darylmitchell/',darylmitchell,name='darylmitchell'),
]