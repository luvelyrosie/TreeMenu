from django.shortcuts import render
from .models import MenuItem


def home(request):
    items = MenuItem.objects.filter(menu='main_menu', parent__isnull=True)
    return render(request, 'tree_menu/home.html', {
        'title': 'Home',
        'menu_items': items
    })