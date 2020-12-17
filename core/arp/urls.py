from django.urls import path
from core.arp.views.categorias.views import *

urlpatterns = [
    path('category/list/', CategoryListView.as_view())
]
