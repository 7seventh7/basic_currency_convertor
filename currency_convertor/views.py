from django.shortcuts import render
import requests



def index(request):

    responce = requests.get(url='https://openexchangerates.org/api/latest.json?app_id=e25bb4b9724d4b13bc092f9eae443c7b').json()
    currencies = responce.get('rates')
    if request.method == 'GET':
        return render(request, 'base.html', {'correncies': currencies})

    if request.method == 'POST':
        ammount = request.POST.get('input')
        input_currncy = request.POST.get("from_cur")
        output_currncy = request.POST.get("in_cur")
        exchange = round((currencies[output_currncy]/currencies[input_currncy])*float(ammount), 2)
        print('ammount=', ammount)
        print('input_currency=', input_currncy, currencies[input_currncy])
        print('output_currency=', output_currncy, currencies[output_currncy])
        print('exchenge=', exchange)
        return render(request, 'base.html', {'correncies': currencies, 'ammount': ammount, 'input_currency': input_currncy, 'output_currncy': output_currncy, 'exchange': exchange})

