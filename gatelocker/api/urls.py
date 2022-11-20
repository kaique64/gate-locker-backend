from rest_framework import routers

from .views import GateViewSet
from django.urls import path, include

urlpatterns = [
    path('gate/open', GateViewSet.open_gate, name='gate'),
    path('gate/close', GateViewSet.close_gate, name='gate'),
]


# router = routers.DefaultRouter()
# router.register('gate/open', GateViewSet.open_gate(), "gate")
# router.register('gate/close', GateViewSet.close_gate, "gate")

# urlpatterns = router.urls