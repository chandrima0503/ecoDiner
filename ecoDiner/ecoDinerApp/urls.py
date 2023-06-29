"""This file contains the code for the urls.py"""
from django.contrib import admin
from django.urls import path
from .views import ( home,
                    restaurant_detail,
                    carbon_footprint,
                    sustainable_menu,
                    waste_reduction,
                    employee_training)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("restaurants/<int:primary_key>/",
        restaurant_detail,
        name="restaurant_detail"),
    path("restaurants/<int:primary_key>/carbon-footprint/",
        carbon_footprint,
        name="carbon_footprint"),
    path("restaurants/<int:primary_key>/sustainable-menu/",
         sustainable_menu,
         name="sustainable_menu"),
    path("restaurants/<int:primary_key>/waste-reduction/",
        waste_reduction,
        name="waste_reduction"),
    path("restaurants/<int:primary_key>/employee-training/",
        employee_training,
        name="employee_training"),
    # path("reports/<int:pk>/", report_view, name="report_view"),
]
