from django.shortcuts import render
from core.arp.models import Category


def myfirstview(request):
    data = {
        'categories': Category.objects.all()
    }
    return render(request, 'home.html', data)
