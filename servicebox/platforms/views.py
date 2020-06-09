from django.shortcuts import render
from django.views.generic import ListView
from .models import Platform


class PlatformListView(ListView):
    model = Platform
