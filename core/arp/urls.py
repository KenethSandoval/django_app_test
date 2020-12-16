from django.urls import path
from core.arp.views.categorias.views import category_list

urlpatterns = [
    path('category/list/', category_list)
]
