from django.shortcuts import render
from .models import Category, Menu
import re

def index(request):
    context = {}
    return render(request, 'index.html', context)

def menu(request):
    cats = Category.objects.order_by('id')
    context = {'cats': cats}
    return render(request, 'menu.html', context)

def about(request):
    return render(request, 'about.html')
