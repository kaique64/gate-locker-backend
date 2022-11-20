import os
import random

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect

from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.response import Response

CLIENT_ID = f'python-mqtt-{random.randint(0, 100000)}'

class GateViewSet(viewsets.ModelViewSet):
    @api_view(['POST'])
    @csrf_protect
    @csrf_exempt
    def open_gate(self):
        print(os.getenv('BROKER_URL'))
        print(os.getenv('BROKER_PORT'))
        print(os.getenv('BROKER_TOPIC'))
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
