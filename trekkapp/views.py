from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
import requests
from django.views import View
from django.views.generic import ListView, DetailView, DeleteView, TemplateView, UpdateView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
import json
from .forms import *
from .models import *
from django.core.mail import send_mail
import re
from django.conf import settings
# Create your views here.
def verify_recaptcha(recaptcha_response):
    secret_key = settings.RECAPTCHA_SECRET_KEY
    payload = {
        'secret': secret_key,
        'response': recaptcha_response
    }
    response = requests.post('https://www.google.com/recaptcha/api/siteverify', data=payload)
    result = response.json()
    return result.get('success')

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
        recaptcha_response = request.POST.get('g-recaptcha-response')
        if verify_recaptcha(recaptcha_response):
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
                pattern=r"^(?:\+91|91)?[789]\d{9}$"
                emailpattern=r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$"
                if(re.match(pattern,request.POST['number'])==None):
                    return render(request,'trekkapp/contact.html',{'form':ContactForm,'number':True})
                elif(re.match(emailpattern,request.POST['email'])==None):
                    return render(request,'trekkapp/contact.html',{'form':ContactForm,'email':True})
                else:
                    return render(request,'trekkapp/contact.html',{'form':ContactForm,'failure':True})
        else:
            return render(request,'trekkapp/contact.html',{'form':ContactForm,'captcha':True})
    else:
        return render(request,'trekkapp/contact.html',{'form':ContactForm})

def personal(request):
    if request.method=='POST':
        form=PersonalForm(request.POST)
        recaptcha_response = request.POST.get('g-recaptcha-response')
        if verify_recaptcha(recaptcha_response):
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
                pattern=r"^(?:\+91|91)?[789]\d{9}$"
                emailpattern=r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$"
                if(re.match(pattern,request.POST['number'])==None):
                    return render(request,'trekkapp/contact.html',{'form':PersonalForm,'number':True})
                elif(re.match(emailpattern,request.POST['email'])==None):
                    return render(request,'trekkapp/contact.html',{'form':PersonalForm,'email':True})
                else:
                    return render(request,'trekkapp/contact.html',{'form':PersonalForm,'failure':True})
        else:
            return render(request,'trekkapp/contact.html',{'form':ContactForm,'captcha':True})
    else:
        return render(request,'trekkapp/contact.html',{'form':PersonalForm})

def view(request):
    userlist=Logger.objects.all().values()
    if request.method=="POST":
        print('done')
        if "username" in request.POST:
            print("its working till here")
            for i in userlist:
                if i["user_name"]==request.POST["username"] and i["password"]==request.POST["password"]:
                    return render(request,'blog/view_blog.html',{"article":Article.objects.all()})
                else:
                    return render(request, 'blog/login.html',{"warning":"error"}) 
    elif request.method=="GET":
        return(render(request,'blog/login.html'))

class Index(ListView):
    model = Article
    template_name = 'blog/index.html'
    context_object_name = 'articles'
    ordering = ['-date']

class Blogspot(ListView):
    model = Article
    template_name = 'blog/blogspot.html'
    context_object_name = 'articles'
    ordering = ['-date']
class DetailArticleView(DetailView):
    model = Article
    template_name = 'blog/blog_post.html'
    context_object_name = 'article'
        

    def get_context_data(self, **kwargs):
        context = super(DetailArticleView,self).get_context_data(**kwargs)
        context['comment_form']=CommentForm(initial={'article':self.object})
        context['comment']=Comment.objects.filter(article=self.object)
        return(context)
    def post(self, request, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.article=self.object
            form.save()
            return HttpResponseRedirect(self.request.path_info)
            
        elif request.is_ajax():
            model_id = self.kwargs['pk']  # Assuming your model uses pk as the primary key
            model = self.get_object()
            action = request.POST.get('action')
            # Logic to update the likes of the model
            # Example:
            if action == 'like':
                    
                if model.likes is not None:
                    model.likes += 1
                else:
                    model.likes = 1
            elif action == 'unlike':
                if model.likes is not None and model.likes > 0:
                    model.likes -= 1
            model.save()
            return JsonResponse({'success': True,'likes': model.likes})
        else:
            print("error is therr",form.errors)
            return self.render_to_response(self.get_context_data(form=form, error_data="error"))
    

class DeleteArticleView(DeleteView):
    model = Article
    template_name = 'blog/blog_delete.html'
    success_url = reverse_lazy('login')

class CreateBlogView(View):
    template_name = 'blog/create_blog.html'

    def get(self, request):
        form = ArticleForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blogspot')
        return render(request, self.template_name, {'form': form})
class UpdateBlogView(UpdateView):
    model=Article
    fields=["title","content","image"]
    template_name='blog/update_blog.html'
    success_url='/edit'

                  
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
