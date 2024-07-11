from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView, DeleteView, TemplateView, UpdateView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
import json
from .forms import *
from .models import *
from django.core.mail import send_mail
# Create your views here.

def index(request):

    return render(request,'trekkapp/trekking.html', {"name":"Monsson", "trekking":Trekking.objects.all(),"cities":City.objects.all(),"festival":Festival.objects.all(),"adventure":Adventure.objects.all(), "camping":Camping.objects.all(),"cycling":Cycling.objects.all(), "tours":Tours.objects.all(),"cities_json":json.dumps(list(City.objects.all().values('name'))) })

def about(request):
    return render(request,'trekkapp/About.html')

class Detailedtrek(DetailView):
    model=City
    template_name="trekkapp/trekdetails.html"

    def get_context_data(self, **kwargs):
        context = super(Detailedtrek,self).get_context_data(**kwargs)
        context["cities"]=City.objects.all()
        context["Gallery"]=Gallery.objects.all().filter(city=self.get_object())
        self.object=self.get_object()
        print(self.object.trekking)
        context["form"]=EnquireForm(initial={'thetrek':self.object.__dict__})
        return context
    
    def post(self, request, **kwargs):
        print(request.POST)
        if 'name' in request.POST:
            self.object = self.get_object()
            print(self.object)
            
            form = EnquireForm(request.POST)
            print(form)
            print(request.POST)
            if form.is_valid():
                print("its valid")
                inquiry = form.save(commit=False)
                inquiry.thetrek = self.object.__dict__  # Assign the City object to the form field
                inquiry.save()
                recipient_email = 'jaideep.technographix@gmail.com'
                subject = 'the trekers enquiry'
                message = f"Name: {form.cleaned_data['name']}\nEmail: {form.cleaned_data['email']}\nMessage: {form.cleaned_data['message']}\nNumber: {form.cleaned_data['number']}\nthe trek: {self.object.__dict__}"
                from_email = form.cleaned_data['email']  # Replace with your email address

                # Send email
                send_mail(subject, message, from_email, [recipient_email])
                return HttpResponseRedirect(self.request.path_info)
            else:
                print(form.errors)  # Print form errors to console for debugging
                return render(request, 'trekkapp/contact.html', {'form': form})
        else:
             return render(request, 'trekkapp/contact.html', {'form': EnquireForm})
class DetailedCycle(DetailView):
    model=Cycling
    template_name="trekkapp/trekdetails.html"

    def get_context_data(self, **kwargs):
        context = super(DetailedCycle,self).get_context_data(**kwargs)
        context["cities"]=City.objects.all()
        context["Gallery"]=Gallery.objects.all().filter(cycling=self.get_object())
        context["form"]=EnquireForm(initial={'thetrek':self.object})
        return context
    
    
    def post(self, request, **kwargs):
        print(request.POST)
        if 'name' in request.POST:
            self.object = self.get_object()
            print(self.object)
            
            form = EnquireForm(request.POST)
            print(form)
            print(request.POST)
            if form.is_valid():
                print("its valid")
                inquiry = form.save(commit=False)
                inquiry.thetrek = self.object.__dict__  # Assign the City object to the form field
                inquiry.save()
                recipient_email = 'jaideep.technographix@gmail.com'
                subject = 'the trekers enquiry'
                message = f"Name: {form.cleaned_data['name']}\nEmail: {form.cleaned_data['email']}\nMessage: {form.cleaned_data['message']}\nNumber: {form.cleaned_data['number']}\nthe trek: { self.object.__dict__}"
                from_email = form.cleaned_data['email']  # Replace with your email address

                # Send email
                send_mail(subject, message, from_email, [recipient_email])
                return HttpResponseRedirect(self.request.path_info)
            else:
                print(form.errors)  # Print form errors to console for debugging
                return render(request, 'trekkapp/contact.html', {'form': form})
        else:
             return render(request, 'trekkapp/contact.html', {'form': EnquireForm})
class DetailedCamp(DetailView):
    model=Camping
    template_name="trekkapp/trekdetails.html"

    def get_context_data(self, **kwargs):
        context = super(DetailedCamp,self).get_context_data(**kwargs)
        context["cities"]=City.objects.all()
        context["Gallery"]=Gallery.objects.all().filter(camping=self.get_object())
        context["form"]=EnquireForm(initial={'thetrek':self.object})
        return context
    def post(self, request, **kwargs):
        print(request.POST)
        if 'name' in request.POST:
            self.object = self.get_object()
            print(self.object)
            
            form = EnquireForm(request.POST)
            print(form)
            print(request.POST)
            if form.is_valid():
                print("its valid")
                inquiry = form.save(commit=False)
                inquiry.thetrek = self.object.__dict__  # Assign the City object to the form field
                inquiry.save()
                recipient_email = 'jaideep.technographix@gmail.com'
                subject = 'the trekers enquiry'
                message = f"Name: {form.cleaned_data['name']}\nEmail: {form.cleaned_data['email']}\nMessage: {form.cleaned_data['message']}\nNumber: {form.cleaned_data['number']}\nthe trek: { self.object.__dict__}"
                from_email = form.cleaned_data['email']  # Replace with your email address

                # Send email
                send_mail(subject, message, from_email, [recipient_email])
                return HttpResponseRedirect(self.request.path_info)
            else:
                print(form.errors)  # Print form errors to console for debugging
                return render(request, 'trekkapp/contact.html', {'form': form})
        else:
             return render(request, 'trekkapp/contact.html', {'form': EnquireForm})
class Detailedtour(DetailView):
    model=Tours
    template_name="trekkapp/trekdetails.html"

    def get_context_data(self, **kwargs):
        context = super(Detailedtour,self).get_context_data(**kwargs)
        context["cities"]=City.objects.all()
        context["Gallery"]=Gallery.objects.all().filter(tours=self.get_object())
        context["form"]=EnquireForm(initial={'thetrek':self.object})
        return context
    
    def post(self, request, **kwargs):
        print(request.POST)
        if 'name' in request.POST:
            self.object = self.get_object()
            print(self.object)
            
            form = EnquireForm(request.POST)
            print(form)
            print(request.POST)
            if form.is_valid():
                print("its valid")
                inquiry = form.save(commit=False)
                inquiry.thetrek = self.object.__dict__  # Assign the City object to the form field
                inquiry.save()
                recipient_email = 'jaideep.technographix@gmail.com'
                subject = 'the trekers enquiry'
                message = f"Name: {form.cleaned_data['name']}\nEmail: {form.cleaned_data['email']}\nMessage: {form.cleaned_data['message']}\nNumber: {form.cleaned_data['number']}\nthe trek: { self.object.__dict__}"
                from_email = form.cleaned_data['email']  # Replace with your email address

                # Send email
                send_mail(subject, message, from_email, [recipient_email])
                return HttpResponseRedirect(self.request.path_info)
            else:
                print(form.errors)  # Print form errors to console for debugging
                return render(request, 'trekkapp/contact.html', {'form': form})
        else:
             return render(request, 'trekkapp/contact.html', {'form': EnquireForm})
        
def contact(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            recipient_email = 'jaideep.technographix@gmail.com'
            subject = 'the trekers contact'
            message = f"Name: {form.cleaned_data['name']}\nEmail: {form.cleaned_data['email']}\nMessage: {form.cleaned_data['message']}\nNumber: {form.cleaned_data['number']}"
            from_email = form.cleaned_data['email']  # Replace with your email address

             # Send email
            send_mail(subject, message, from_email, [recipient_email])
            return render(request,'trekkapp/contact.html',{'form':ContactForm,'success':True})
        else:
            return render(request,'trekkapp/contact.html',{'form':ContactForm,'failure':True})
    else:
        return render(request,'trekkapp/contact.html',{'form':ContactForm})

def personal(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            recipient_email = 'jaideep.technographix@gmail.com'
            subject = 'the trekers custom trek'
            message = f"Name: {form.cleaned_data['name']}\nEmail: {form.cleaned_data['email']}\nMessage: {form.cleaned_data['message']}\nNumber: {form.cleaned_data['number']}"
            from_email = form.cleaned_data['email']  # Replace with your email address

            # Send email
            send_mail(subject, message, from_email, [recipient_email])
            return render(request,'trekkapp/contact.html',{'form':PersonalForm,'success':True})
        else:
            return render(request,'trekkapp/contact.html',{'form':PersonalForm,'failure':True})
    else:
        return render(request,'trekkapp/contact.html',{'form':PersonalForm})
                  
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
