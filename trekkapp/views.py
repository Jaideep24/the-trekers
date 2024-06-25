from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView, DeleteView, TemplateView, UpdateView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
#from .forms import *
from .models import *
# Create your views here.

def index(request):
    return render(request,'trekkapp/trekking.html', {"name":"Monsson", "trekking":Trekking.objects.all(),"cities":City.objects.all(),"festival":Festival.objects.all(),"adventure":Adventure.objects.all(), "camping":Camping.objects.all(),"cycling":Cycling.objects.all(), "tours":Tours.objects.all() })

class Detailedtrek(DetailView):
    model=City
    template_name="trekkapp/trekdetails.html"

    def get_context_data(self, **kwargs):
        context = super(Detailedtrek,self).get_context_data(**kwargs)
        context["cities"]=City.objects.all()
        return context