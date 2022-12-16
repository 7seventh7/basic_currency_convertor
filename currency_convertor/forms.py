from django import forms
from django.contrib.sites import requests
from django.shortcuts import render
import requests

from .models import *


class AddConvertationForm(forms.Form):


    currency_in = forms.ChoiceField()
    currency_out = forms.CharField()
    currency_in_ammount = forms.DecimalField(decimal_places=2, max_digits=10)
    course = forms.DecimalField(decimal_places=2, max_digits=10)
