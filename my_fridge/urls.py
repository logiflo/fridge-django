"""Defines the URLS patterns for my_fridge
"""

from django.urls import path
from . import views

urlpatterns = [
    # Home page
    path('', views.home, name='home'),
    path('food/', views.food, name='food'),
    path('food_out/', views.food_out, name='food_out'),
    path('add_food/', views.add_food, name='add_food'),
    path('each_food/<food_id>', views.each_food, name='each_food'),
    path('add_quantity/<food_id>', views.add_quantity, name='add_quantity'),
    #path('remove_quantity/<food_id>', views.remove_quantity, name='remove_quantity'),
    path('essencials', views.essencials, name='essencials'),
    path('add_essencials', views.add_essencials, name='add_essencials'),
    path('add_quantity_essencials/<essencials_id>', views.add_quantity_essencials, name='add_quantity_essencials'),
    path('add_essencials_to_fridge', views.add_essencials_to_fridge, name='add_essencials_to_fridge'),
    path('change_units/<food_id>', views.change_units, name='change_units'),
    path('remove_food/<food_id>', views.remove_food, name='remove_food'),
    path('remove_essencial/<essencials_id>', views.remove_essencial, name='remove_essencial'),
    ]
