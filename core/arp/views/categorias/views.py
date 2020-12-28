from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse, HttpResponseRedirect
from django.urls import reverse_lazy

from core.arp.models import Category
from core.arp.forms import CategoryForm


class CategoryListView(ListView):
    model = Category
    template_name = 'category/list.html'
  
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
         
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = Category.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Categorías'
        context['create_url'] = reverse_lazy('arp:category_create')
        context['list_url'] = reverse_lazy('arp:category_list')
        context['entity'] = 'Categorias'
        return context


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/create.html'
    success_url = reverse_lazy('arp:category_list')

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                if form.is_valid():
                    form.save()
                else: 
                    data = form.errors
            else:
                data['error'] = 'No ha ingresado ninguna opcion'

        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear una Categoria'
        context['entity'] = 'Categorias'
        context['list_url'] = reverse_lazy('arp:category_list')
        context['action'] = 'add'
        return context

class CategoryUpdateView(UpdateView): 
    model = Category
    form_class = CategoryForm
    template_name = 'category/create.html'
    success_url = reverse_lazy('arp:category_list')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                if form.is_valid():
                    form.save()
                else: 
                    data = form.errors
            else:
                data['error'] = 'No ha ingresado ninguna opcion'

        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar una Categoria'
        context['entity'] = 'Categorias'
        context['list_url'] = reverse_lazy('arp:category_list')
        context['action'] = 'edit'
        return context
