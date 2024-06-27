from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView, DeleteView, TemplateView, UpdateView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
import json
#from .forms import *
from .models import *
# Create your views here.

def index(request):
    
    return render(request,'trekkapp/trekking.html', {"name":"Monsson", "trekking":Trekking.objects.all(),"cities":City.objects.all(),"festival":Festival.objects.all(),"adventure":Adventure.objects.all(), "camping":Camping.objects.all(),"cycling":Cycling.objects.all(), "tours":Tours.objects.all(),"cities_json":json.dumps(list(City.objects.all().values('name'))) })

class Detailedtrek(DetailView):
    model=City
    template_name="trekkapp/trekdetails.html"

    def get_context_data(self, **kwargs):
        context = super(Detailedtrek,self).get_context_data(**kwargs)
        context["cities"]=City.objects.all()
        return context
class DetailedCycle(DetailView):
    model=Cycling
    template_name="trekkapp/trekdetails.html"

    def get_context_data(self, **kwargs):
        context = super(DetailedCycle,self).get_context_data(**kwargs)
        context["cities"]=City.objects.all()
        return context
class DetailedCamp(DetailView):
    model=Camping
    template_name="trekkapp/trekdetails.html"

    def get_context_data(self, **kwargs):
        context = super(DetailedCamp,self).get_context_data(**kwargs)
        context["cities"]=City.objects.all()
        return context
class Detailedtour(DetailView):
    model=Tours
    template_name="trekkapp/trekdetails.html"

    def get_context_data(self, **kwargs):
        context = super(Detailedtour,self).get_context_data(**kwargs)
        context["cities"]=City.objects.all()
        return context
def data_city(request):
    data = list(City.objects.all().values())  # Convert queryset to list of dictionaries
    return JsonResponse(data, safe=False)
def data_camping(request):
    data = list(Camping.objects.all().values())  # Convert queryset to list of dictionaries
    return JsonResponse(data, safe=False)
def data_cycling(request):
    data = list(Cycling.objects.all().values())  # Convert queryset to list of dictionaries
    return JsonResponse(data, safe=False)
def data_tours(request):
    data = list(Tours.objects.all().values())  # Convert queryset to list of dictionaries
    return JsonResponse(data, safe=False)