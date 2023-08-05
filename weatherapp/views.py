from django.shortcuts import render
from django.contrib import messages
import requests
import datetime


def home(request):
    # appid = '95c9c6eab7ea5475d073649ff78be209'
    # URL = 'https://api.openweathermap.org/data/2.5/weather'
    # PARAMS = {'q':'amsterdam','appid': 'appid', 'units': 'metric'} 
    # r = requests.get(url=URL, params=PARAMS)
    # res = r.json()
    # description = res['weather'][0]['description']
    # icon = res['weather'][0]['icon']
    # temp = res['main']['temp']



    # return render(request, 'weatherapp/index.html', {'description':description, 'icon':icon, 'temp':temp} )
    if 'city' in request.POST:
         city = request.POST['city']
    else:
         city = None     
    
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=95c9c6eab7ea5475d073649ff78be209'
    PARAMS = {'units':'metric'}
    
    try:
          data = requests.get(url,params=PARAMS).json()
          description = data['weather'][0]['description']
          icon = data['weather'][0]['icon']
          temp = data['main']['temp']
          day = datetime.date.today()

          return render(request,'weatherapp/index.html' , {'description':description , 'icon':icon ,'temp':temp , 'day':day , 'city':city })
    
    except KeyError:
          exception_occured = True
          messages.error(request,'Entered data is not available to API')   
          # city = 'indore'
          # data = requests.get(url,params=PARAMS).json()
          
          # description = data['weather'][0]['description']
          # icon = data['weather'][0]['icon']
          # temp = data['main']['temp']
          day = datetime.date.today()

          return render(request,'weatherapp/index.html' ,{'description':'clear sky', 'icon':'01d'  ,'temp':25 , 'day':day , 'city':'indore' , 'exception_occured':exception_occured } )
               
    
    