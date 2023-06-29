"""This file contains the code for the models.py"""
from django.db import models

class Restaurant(models.Model):
    """This module contains the model for the Restaurant."""
    objects = models.Manager()
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2, choices=[('UK', 'United Kingdom')], default='UK')
    zip_code = models.CharField(max_length=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}"

    def to_dict(self):
        """This module returns the model for the Restaurant Footprint."""
        return {
            "name": self.name,
            "address": self.address,
            "city": self.city,
            "state": self.state,
            "zip_code": self.zip_code,
            "created_at": str(self.created_at),
            "updated_at": str(self.updated_at),
            "description": self.description,
        }

class CarbonFootprint(models.Model):
    """This module contains the model for the Carbon Footprint."""
    objects = models.Manager()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    energy_consumption = models.FloatField()
    water_consumption = models.FloatField()
    waste_production = models.FloatField()
    date_submitted = models.DateTimeField(auto_now_add=True)

    def to_dict(self):
        """This module returns the model for the Carbon Footprint."""
        return {
            "restaurant": self.restaurant,
            "energy_consumption": self.energy_consumption,
            "water_consumption": self.water_consumption,
            "waste_production": self.waste_production,
            "date_submitted": self.date_submitted,
        }

class SustainableMenu(models.Model):
    """This module contains the model for the Sustainable Menu."""
    objects = models.Manager()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    ingredients = models.TextField(default='')
    nutritional_analysis = models.TextField(default='')
    
    def to_dict(self):
        """This module returns the model for the Sustainable Menu."""
        return {
            "restaurant": self.restaurant,
            "ingredients": self.ingredients,
            "nutritional_analysis": self.nutritional_analysis,
        }

class WasteReduction(models.Model):
    """This module contains the model for the Waste Reduction."""
    objects = models.Manager()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    waste_management = models.TextField()
    inventory_management = models.TextField()

    def to_dict(self):
        """This module returns the model for the Waste Reduction."""
        return {
            "restaurant": self.restaurant,
            "waste_management": self.waste_management,
            "inventory_management": self.inventory_management,
        }

class EmployeeTraining(models.Model):
    """This module contains the model for the Employee Training."""
    objects = models.Manager()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    resources = models.TextField()
    engagement_tools = models.TextField()

    def to_dict(self):
        """This module returns the model for the Waste Reduction."""
        return {
            "restaurant": self.restaurant,
            "resources": self.resources,
            "engagement_tools": self.engagement_tools,
        }
