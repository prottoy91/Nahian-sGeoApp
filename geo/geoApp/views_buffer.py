#!/usr/bin/env python3
from django.shortcuts import render, redirect
import os
import folium
from django.http import HttpResponse
import numpy as np
import websockets
import asyncio
import aiohttp
from aiohttp import web
from django.template import RequestContext

from django.views.decorators.csrf import csrf_exempt



    
@csrf_exempt
def home(request):
    nam = 'c'
    rss=0

    shp_dir = os.path.join(os.getcwd(),'media','shp')

    # folium
    m = folium.Map(location=[23.762433884,90.3709100303],zoom_start=20, max_zoom=40)

    ## style
    style_floor = {'fillColor': '#228B22', 'color': '#228B22','weight':'0.5'}
    style_C4 = { 'color': 'yellow','weight':'0.5'}
    
    
    if request.method == 'POST':
        print('recieved')
        if 'nam' in request.POST:
            nam = request.POST['nam']
            rss=request.POST['rss']
                
            
            
    #coord = get_gps
    #hurr.append(rss)
    print(nam,rss)
   # np.savetxt('readings_8.csv', hurr, delimiter=',', fmt='%s')
    ## adding to views
   
    folium.GeoJson(os.path.join(shp_dir,'floor.geojson'),name='Floor',style_function=lambda x:style_floor).add_to(m)
    folium.GeoJson(os.path.join(shp_dir,'C4.geojson'),name='Floor Plan',style_function=lambda x:style_C4).add_to(m)
    folium.LayerControl().add_to(m)

    ## exporting
    m=m._repr_html_()
    context = {'my_map': m}
	
    ## rendering
    return render(request,'geoApp/home.html',context)

