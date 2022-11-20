import os
import time
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
                return Response({
                    "status": 500,
                    "message": "Failed to connect on MQTT"
                }, status=500)

            print("Connected to MQTT Broker!")
        
        client = mqtt_client.Client(client_id)
        client.on_connect = on_connect
        client.connect(url, port)
        return client
    
class MQTTService:
    def publish(self, client, topic, msg):
        result = client.publish(topic, msg)

        status = result[0]
        if status != 0:
            print(f"Failed to send message to topic {topic}")
            return Response({
                "status": 500,
                "message": f"Failed to send message to topic {topic}"
            }, status=500)

        print(f"Send `{msg}` to topic `{topic}`")


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
