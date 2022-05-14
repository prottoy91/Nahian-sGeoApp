#!/usr/bin/env python3


#def get_gps(request):
    #json_data = json.dumps({"HTTPRESPONSE":1})
    # json data is just a JSON string now. 
    #return HttpResponse('success')
    #if request.method == 'POST':
       #if 'lat' in request.POST:
          #  lat = request.POST['lat']
           ## print('Hello')
            #print(f'Latitude is: {lat}')
            #return lat
           # msg = f'success' 
            #return HttpResponse('success')
            #if 'lng' in request.POST:
              #  lng = request.POST['lng'] 
            # doSomething with data here...
                
                #return lat,lng
    # nothing went well#
    #else:
       # return HttpRespsonse('FAIL!')
# Create your views here.
#import operator
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

from branca.element import Element
from folium import Map, LayerControl
#from folium import plugins
#from folium.map import (FeatureGroup, Icon, Layer, Marker, Tooltip, Popup)

#import sys
#sys.path.insert(0,'/home/Prottoy/Desktop/ToSend/geo/ToSend2/App/geo/geoApp/')
#from consumers import tr
   
@csrf_exempt
def home(request):
    #nam = 'c'
   # rss=0 

    #shp_dir = os.path.join(os.getcwd(),'media','shp')

    # folium
   # m = folium.Map(location=[23.762433884,90.3709100303],zoom_start=19, max_zoom=40)#, #crs='EPSG3857')23.762428468993015 90.37089846810431
    #m=m._repr_html_()
    #c={'hh' : m}
   # mkr=folium.Marker(
   #     location=[23.762433884,90.3709100303], popup=['My house']
   # ).add_to(m)
    #obj.template_vars.get('custom_markers')[0]

    ## style
   # style_floor = {'fillColor': '#228B22', 'color': '#228B22','weight':'0.5'}
   # style_C4 = { 'color': 'yellow','weight':'0.5'}
    
    
   # if request.method == 'POST':
    #    print('recieved')
    #    if 'nam' in request.POST:
    #        nam = request.POST['nam']
     #       rss=request.POST['rss']
                
            
            
    #coord = get_gps
    #hurr.append(rss)
   # print(nam,rss)
   # np.savetxt('readings_8.csv', hurr, delimiter=',', fmt='%s')
    ## adding to views
   #
   # folium.GeoJson(os.path.join(shp_dir,'C4.geojson'),name='Floor',style_function=lambda x:style_floor).add_to(m)
   # folium.GeoJson(os.path.join(shp_dir,'floor.geojson'),name='Floor Plan',style_function=lambda x:style_C4).add_to(m)
    #folium.LayerControl().add_to(m)
  #  transformer = Transformer.from_crs("epsg:3857","epsg:4326")
    #plugins.TimestampedGeoJson(
     #   { "type": "FeatureCollection",'features': [
     # {
      #  'type': 'Feature',
      #  'geometry': {
      #    'type': 'LineString',
      #    'coordinates': [[23.762433884,90.3719100303],[23.762423884,90.3709150303],[23.762433884,90.3709900303]],
      #    },
      #  'properties': {
      #    'times': [1435708800000, 1435795200000, 1435881600000]
      #    }
      #  }
     # ]},
     #   period="P1D", add_last_point=False, 
   # ).add_to(m)
    #m = folium.Map(location=[17.106, -66.402], zoom_start=8, width=800, height=300)
   # plugins.TimestampedGeoJson(
      #  { "type": "FeatureCollection", "features": [os.path.join(shp_dir,'C4.geojson'),os.path.join(shp_dir,'floor.geojson')]},
     #   period="P1D", add_last_point=False, 
   # ).add_to(m)
    #pos=tr
    #print(tr)
    #out=transformer.transform(10060042.40,2724485.59)
    #mkr=folium.Marker(
     #   location=[out[0],out[1]], popup=['My house']
   ##).add_to(m)
        
        #folium.LayerControl().add_to(m)
        #return []
    #folium.removeLayer(mkr)
    ## exporting
    #feature_group = FeatureGroup(name="Some icons")
    #Marker(location=[23.762433883,90.3709100303], popup="Mt. Hood Meadows").add_to(feature_group)

    #Marker(location=[23.762493884,90.3709100309], popup="Timberline Lodge").add_to(feature_group)

    #feature_group.add_to(m)
    #js = """{{kwargs['my_map']}}.on('click', function(e) {  alert(e.latlng);});"""
                                            
    #m.get_root().script.add_child(Element(js))
   # LayerControl().add_to(m)
   # my_js = '''
    #console.log('working perfectly')
    #'''
    #m.get_root().script.add_child(Element(my_js))
  #  m=m._repr_html_()
    #m.save('geoApp/home.html')
   # context = {'my_map': m}
	
    ## rendering
    return render(request,'geoApp/home.html')

