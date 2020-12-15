from django.urls import path
from core.arp.views import myfirstview

urlpatterns = [
    path('uno/', myfirstview)
]
