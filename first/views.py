from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import usd_to_currency,c,dec_currency

from first.models import signin
from first.forms import signin2

# Create your views here.

def base(request):
    return render(request,'base.html')

def login(request):
    if request.method == 'POST':
        ss=signin2(request.POST)
        if ss.is_valid():
            ss.save()
            name=ss.cleaned_data.get('fullname')

            return render(request,'base.html', {'a':"Welcome"+"     "+name})

        else:
            return HttpResponse('<h>fail signin</h>')

    else:
        form=signin2()
        return render(request,'login.html',{'form':form})


r=' '
def postt(request):

    if request.method == 'POST':

          obj=c.objects.get(id=2)
          print(obj)
          number=float(request.POST.get('num'))
          print(number)

          switch={
              #convert the currency to USD
                     'USD':number*obj.USD,
                     'IQD':number*obj.IQD,
                     'EUR':number*obj.EUR,
                     'MAD':number*obj.MAD,
               }
          v = request.POST['drop1']

          result1=switch.get(v)
          obj2=usd_to_currency.objects.get()

          switcher = {

              'USD':result1*obj2.USD,

              'IQD':result1*obj2.IQD,
              'EUR':result1*obj2.EUR,
              'MAD':result1*obj2.MAD,
         }
          v2 = request.POST['drop2']

          if v == v2:
                result2=number
          else:
                result2=switcher.get(v2)

          return render(request,'translate.html',{'result':result2,'number':str(number)+' '+v+'=',
                                                  'v2':v2})

    return render(request,'translate.html')



def measure(request):
    if request.method == 'POST':
        number = float(request.POST.get('num'))

        switch = {
            # convert to meter
            'KM': number *1000 ,
            'M': number *1,
            'CM': number *0.01 ,
            'MM': number * 0.001 ,
            'MI': number * 1609.344,
            'FT': number * 0.3,
        }
        v3= request.POST['drop3']
        result13= switch.get(v3)

        switcher = {
            # convert to measure that chose it in second select
            'KM': result13*0.001 ,
            'M': result13 *1 ,
            'CM': result13  * 100 ,
            'MM': result13  *1000,
            'MI': result13 *(6.21*pow(10,-4)),
            'FT': result13  *3.28 ,
        }
        v4= request.POST['drop4']

        if v3 == v4:
            result3 = number
        else:
            result3 = switcher.get(v4)

        return render(request,'measure.html',{'r':result3,'number':str(number)+' '+v3+'=',
                                                  'v4':v4})
    return render(request,'measure.html')





def weight(request):

    if request.method == 'POST':
        number = float(request.POST.get('num'))

        switch = {
            # convert to kelogram
            'طن': number *1000,
            'كيلوجرام': number *1,
            'جرام': number *0.001,
            'رطل': number *0.453592,
            'اونصة': number *0.0283495 ,

        }
        v3= request.POST['drop4']
        result13= switch.get(v3)

        switcher = {
            # convert to weight that chose it in second select
            'طن': result13 *0.001,
            'كيلوجرام': result13 *1,
            'جرام': result13 *1000,
            'رطل': result13 *2.20462,
            'اونصة': result13 *35.274,

        }
        v4= request.POST['drop5']

        if v3 == v4:
            result3 = number
        else:
            result3 = switcher.get(v4)

        return render(request,'wight.html',{'r':result3,'number':str(number)+' '+v3+'=',
                                                  'v4':v4})
    return render(request,'wight.html')




































def wight(request):
    return render(request,'measure.html')

