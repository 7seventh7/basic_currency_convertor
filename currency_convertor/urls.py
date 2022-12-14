from django.contrib import admin
from django.urls import path
from currency_convertor.views import index

urlpatterns = [

    path('', index, name = 'index'),
]
