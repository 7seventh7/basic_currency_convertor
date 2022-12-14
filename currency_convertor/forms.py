from django import forms
from .models import *

class AddConvertationForm(forms.Form):


    currency_in = forms.CharField(
        max_length=3
    )
    currency_out = forms.CharField(
        max_length=3
    )
    currency_in_ammount = forms.DecimalField(
        decimal_places=2, max_digits=10
    )
    course = forms.DecimalField(
        decimal_places=2, max_digits=10
    )
