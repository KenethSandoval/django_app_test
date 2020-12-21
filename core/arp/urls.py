from django.urls import path
from core.arp.views.categorias.views import *

app_name = 'arp'

urlpatterns = [
    path('category/list/', CategoryListView.as_view(), name='category_list'),
    path('category/add/', CategoryCreateView.as_view(), name='category_create'),
]
