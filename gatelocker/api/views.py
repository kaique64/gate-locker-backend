import os
import random
from paho.mqtt import client as mqtt_client

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect

from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.response import Response

BROKER_URL = os.getenv('BROKER_URL')
BROKER_PORT = os.getenv('BROKER_PORT')
BROKER_TOPIC = os.getenv('BROKER_TOPIC')

class MQTTConnection:
    def connect(self, url, port):
        client_id = f'python-mqtt-{random.randint(0, 100000)}'

        def on_connect(client, userdata, flags, rc):
            if rc != 0:
                print("Failed to connect, return code %d\n", rc)
            print("Connected to MQTT Broker!")
        
        client = mqtt_client.Client(client_id)
        client.on_connect = on_connect
        client.connect(url, port)
        return client


class GateViewSet(viewsets.ModelViewSet):
    @api_view(['POST'])
    @csrf_protect
    @csrf_exempt
    def open_gate(self):
        return Response({
            "status": 200,
            "open": True,
            "close": False,
        }, status=200)

    @api_view(['POST'])
    @csrf_protect
    @csrf_exempt
    def close_gate(self,):
        return Response({
            "status": 200,
            "open": False,
            "close": True,
        }, status=200)