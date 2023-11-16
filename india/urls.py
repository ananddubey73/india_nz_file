from india.views import *
from django.urls import path
app_name='ind'
urlpatterns=[
    path('virat/',virat,name='virat'),
    path('shreyasiyer/',shreyasiyer,name='shreyasiyer'),
]