from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='home'),
    path('catalog', views.catalog, name='cat'),
    path('recipes', views.recipes, name='recipes'),
    path('logout', views.recipes, name='logout'),

]
