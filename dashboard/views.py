from django.shortcuts import render, redirect
from . models import Smart_Meter_Data
from . forms import Smart_Meter_DataForm
from django.contrib.auth.decorators import login_required
import geocoder
import folium
from folium import plugins
from bs4 import BeautifulSoup
import urllib.request
import re


# Create your views here.


@login_required(login_url='user-login')
def index(request):
    data = Smart_Meter_Data.objects.all()
    context = {
        'data': data,
        # 'red_alert': red_alert,
    }
    return render(request, 'dashboard/index.html', context)


@login_required(login_url='user-login')
def detail(request, pk):
    data = Smart_Meter_Data.objects.get(id=pk)
    m = folium.Map(location=[7.8, -1], zoom_start=6)
    lat = data.latitude
    lng = data.longitude
    location = data.location
    folium.Marker(location=[lat, lng],
                  tooltip='Click for more',
                  popup=location,
                  icon=folium.Icon(
                          color='red', prefix='fa', icon='bolt')
                  ).add_to(m)
    plugins.Fullscreen().add_to(m)
    m = m._repr_html_()
    context = {
        'data': data,
        'm': m,
    }
    return render(request, 'dashboard/detail.html', context)


def add_meter(request):
    if request.method == 'POST':
        form = Smart_Meter_DataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-index')
    else:
        form = Smart_Meter_DataForm()
    context = {
        'form': form,
    }
    return render(request, 'dashboard/addmeter.html', context)
