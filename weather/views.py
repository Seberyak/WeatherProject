from django.shortcuts import render
from requests import get as req
from .models import City
from .forms import CityForm


# Create your views here.

def index(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=6090349fafc4beaeda35cb262e50f238&units=metric'

    cities = City.objects.all()
    all_cities = list()

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    for city in cities:
        response = req(url.format(city.name)).json()
        city_info = {
            'city': response['name'],
            'temp': response['main']['temp'],
            'icon': response['weather'][0]['icon']
        }
        all_cities.insert(0, city_info)
        # print('-------------------------------------------------------')
        # print(city_info)
    context = {'all_info': all_cities, 'form': form}

    return render(request, 'weather/index.html', context)
