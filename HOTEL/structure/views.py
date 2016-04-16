from django.shortcuts import render
from django.views.generic import ListView
from structure.models import House

# Create your views here.
class HouseList(ListView):
    model = House
    bs_length = 1
