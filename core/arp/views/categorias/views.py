from django.shortcuts import render
from core.arp.models import Category
from django.views.generic import ListView

class CategoryListView(ListView):
    model = Category
    template_name = 'category/list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Categorías'
        return context
