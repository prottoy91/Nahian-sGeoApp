#!/usr/bin/env python3
from django.shortcuts import render, redirect
import asyncio
import json
#from channels.consumer import AsyncConsumer
from random import randint
from time import sleep
from channels.generic.websocket import WebsocketConsumer
import math
from asgiref.sync import async_to_sync
from pyproj import Transformer
import numpy as np
#v=[0,0,0]
#def myfunc(rss,name):
  #  if name=='Prottoy':
  #      v[0]=rss
                
   # elif name=='Propar':
    #    v[1]=rss
                
   # else:
    #    v[2]=rss
    #print(v)


class PracticeConsumer(WebsocketConsumer):
    
    #connected=set()
    def connect(self):
        # when websocket connects
        print("connected")
        self.room_group_name='nav'
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()
                       



       # self.send(text_data=json.dumps({
           # "rss":"[-50,-60,-70]"}))




  
    def receive(self,text_data):
        # when a message is received from websocket
        #text_data_json = json.dumps(text_data)
        #text_data_json=open(text_data,'r')
        #out=self.transformer.transform(234234,234234)
        #print(out)
        
        try:
            text_data_json = json.loads(text_data)
            #name=text_data_json['nam']
            rss=text_data_json['rss']
            if (rss[1]<0):
                print('RSSI:',rss,': This is from a cell phone')
            else:
                print('Position:',rss,':This is from Matlab')
            #print(self.channel_name)
            #self.send(text_data=json.dumps({
               # "rss":rss}))
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                     'type':'chat_message',
                     'rss':rss,
                     #'sender_channel_name':self.channel_name
                }
            )
                
            #for conn in self:
                #    if conn != self:
                 #       conn.send(str(rss))
            #if name =='Prottoy':
            #    pro=rss
                
           # elif name =='Propar':
           #     par=rss
                
           # elif name =='Propatch':
           #     patch=rss
            #print(v)
            #myfunc(rss,name)
           # if math.isnan(pro)==False and math.isnan(par)==False and math.isnan(patch)==False:
          #  v=[pro,par,patch]
           # print(v)
         #   if v[0] != 0 and v[1] != 0 and v[2] != 0:
         #       for conn in self:
         #               if conn != self:
          #                  conn.send(str(v))
          #                  v=[0,0,0]
        except ValueError as e:
            position=text_data
            print('Position:',text_data,': This is from Matlab')
            #c={'pos':position}
            #return render(request,'geoApp/home.html',c)

        
        #print("Received message from client: " + message)

        #self.send(text_data=json.dumps({
           # "type": "sending",
          #  "message":"I recieved your message!"}))
        
        
        
    def chat_message(self,event):
        #from pyproj import Transformer
        rss=event['rss']
        transformer = Transformer.from_crs("epsg:3857","epsg:4326")
        #out=transformer.transform(rss[0],rss[1])
        #print(rss[0],rss[1])
        if (rss[1]>0):
            out=transformer.transform(rss[0],rss[1])
            self.send(text_data=json.dumps({
                'rss':out
            }))
            print("Lat and long",out)
        else:
            #rss=event['rss']
            self.send(text_data=json.dumps({
            'rss':rss
            }))
    
    def disconnect(self, event):
        # when websocket disconnects
        print("disconnected", event)
