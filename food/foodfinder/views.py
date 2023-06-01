from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'foodfinder/index.html')


def catalog(request):
    return render(request, 'foodfinder/catalog.html')


def recipes(request):
    return render(request, 'foodfinder/recipes.html')


def logout(request):
    return render(request, 'foodfinder/recipes.html')
