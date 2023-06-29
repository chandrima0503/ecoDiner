"""This file contains the code for the views.py"""
from django.shortcuts import render
from .models import Restaurant, CarbonFootprint, SustainableMenu, WasteReduction, EmployeeTraining
import json

def home(request):
    """This module contains the code for the Home."""
    restaurants = Restaurant.objects.all()
    return render(request, 'home.html', {'restaurants': restaurants})


def restaurant_detail(request, primary_key):
    """This module contains the code for the restaurants details."""
    restaurant = Restaurant.objects.get(id=primary_key)

    restaurant_carbon_footprints = CarbonFootprint.objects.filter(restaurant=restaurant)
    carbon_emission = 0.0
    for restaurant_carbon_footprint in restaurant_carbon_footprints:

        #calculating carbon emission
        carbon_emission += float(restaurant_carbon_footprint.energy_consumption) * 0.5
        carbon_emission += float(restaurant_carbon_footprint.water_consumption) * 0.25
        carbon_emission += float(restaurant_carbon_footprint.waste_production) * 0.125
        print(carbon_emission)

    return render(
            request,
                'restaurant_detail.html',
                {
                      'restaurant': restaurant,
                      'carbon_footprint': carbon_emission

                },
            )

def carbon_footprint(request, primary_key):
    """This module contains the code for the carbon footprint."""
    restaurant_carbon_footprints = CarbonFootprint.objects.filter(restaurant=primary_key)
    print(restaurant_carbon_footprints)

    return render(
        request,
        'carbon_footprint.html',
        {
            'restaurant_carbon_footprint_array': restaurant_carbon_footprints
        },
    )

def sustainable_menu(request, primary_key):
    """This module contains the code for the sustainable menu."""
    restaurant_sustainable_menu = SustainableMenu.objects.get(restaurant=primary_key)
    ingredients = (
        restaurant_sustainable_menu.ingredients
        ).replace("[","").replace("]","").split(",")
    nutritional_analysis = (
        restaurant_sustainable_menu.nutritional_analysis
        ).replace("[","").replace("]","").replace("{","").split("},")
    return render(
        request,
        'sustainable_menu.html',
        {
            'restaurant_sustainable_menu': restaurant_sustainable_menu,
            'ingredients': ingredients,
            'nutritional_analysis': nutritional_analysis
        },
    )

def waste_reduction(request, primary_key):
    """This module contains the code for the waste reduction."""
    restaurant_waste_reduction = WasteReduction.objects.get(restaurant=primary_key)
    inventory = (
        restaurant_waste_reduction.inventory_management
                 ).replace("[","").replace("]","").split(",")
    return render(
        request,
        'waste_reduction.html',
        {
            'restaurant_waste_reduction': restaurant_waste_reduction,
            'inventory': inventory,
        },
    )

def employee_training(request, primary_key):
    """This module contains the code for the employee training."""
    restaurant_employee_training = EmployeeTraining.objects.get(restaurant=primary_key)
    resources = (restaurant_employee_training.resources).replace("[","").replace("]","").split(",")
    engagement_tools = (
        restaurant_employee_training.engagement_tools
        ).replace("[","").replace("]","").split(",")
    return render(
        request,
        'employee_training.html',
        {
            'restaurant_employee_training': restaurant_employee_training,
            'resources': resources,
            'engagement_tools': engagement_tools
        },
    )
