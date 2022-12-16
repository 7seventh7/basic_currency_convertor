from django.shortcuts import render
import requests

from currency_convertor.forms import AddConvertationForm



def index(request):

    responce = requests.get(url='https://openexchangerates.org/api/latest.json?app_id=e25bb4b9724d4b13bc092f9eae443c7b').json()
    currencies = responce.get('rates')
    if request.method == 'GET':

        return render(request, 'base.html', {'correncies': currencies})

    if request.method == 'POST':
        if request.POST.get('from_cur') == 'Choose Input Currency' or request.POST.get('from_cur') == '!!CHOOSE CURRENCY!!' :
            error = 'please choose input currency!'
            if request.POST.get('input'):
                input = request.POST.get('input')
            return render(request, 'base.html', {'correncies': currencies, 'error': error, 'input': input})
        if request.POST.get('in_cur') == 'Choose Output Currency' or request.POST.get('in_cur') == '!!CHOOSE CURRENCY!!' :
            error = 'please choose output currency!'
            if request.POST.get('input'):
                input = request.POST.get('input')
            return render(request, 'base.html', {'correncies': currencies, 'error': error, 'input': input})
        if  request.POST.get('input') == None:
            error_type = 'not valid data'

            input_currncy = request.POST.get("from_cur")
            output_currncy = request.POST.get("in_cur")
            return render(request, 'base.html', {'correncies': currencies, 'error_type': error_type, 'input_currency': input_currncy, 'output_currncy': output_currncy})

        ammount = request.POST.get('input')
        input_currncy = request.POST.get("from_cur")
        output_currncy = request.POST.get("in_cur")
        exchange = round((currencies[output_currncy]/currencies[input_currncy])*float(ammount), 2)
        print('ammount=', ammount)
        print('input_currency=', input_currncy, currencies[input_currncy])
        print('output_currency=', output_currncy, currencies[output_currncy])
        print('exchenge=', exchange)
        return render(request, 'base.html', {'correncies': currencies, 'ammount': ammount, 'input_currency': input_currncy, 'output_currncy': output_currncy, 'exchange': exchange})

def work_with_form(request):
    form = AddConvertationForm()

    responce = requests.get(
        url='https://openexchangerates.org/api/latest.json?app_id=e25bb4b9724d4b13bc092f9eae443c7b').json()
    currencies = responce.get('rates')  #<----------------------THIS LIST

    if request.method == 'GET':
        form.course = 2.22 #<-------------------WHANT TO SEE IN THIS FIELD
        return render(request, 'base_form.html', {'form': form})

    return render(request, 'base_form.html', {'form': form})