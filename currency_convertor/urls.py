from django.urls import path

from .views import *

urlpatterns = [

    path('', index, name='index'),
    path('form', work_with_form, name='form'),

]
