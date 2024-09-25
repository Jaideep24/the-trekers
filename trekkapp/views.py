from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
import requests
from django.views import View
from django.views.generic import ListView, DetailView, DeleteView, TemplateView, UpdateView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
import json
from .forms import *
from .models import *
from django.core.mail import send_mail
import re
from django.conf import settings
from PIL import Image, ImageDraw, ImageFont, ImageOps
import random
import string
from io import BytesIO
import datetime
from django.core.files.storage import default_storage

def upload_image(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']
        image_name = default_storage.save(image.name, image)
        image_url = default_storage.url(image_name)
        return JsonResponse({'success': True, 'imageUrl': image_url})
    return JsonResponse({'success': False})

# Create your views here.
def generate_captcha_text(length=6):
    excluded_characters = 'Il1O0'
    
    # Create a pool of characters, excluding the unwanted ones
    characters = ''.join(c for c in string.ascii_letters + string.digits if c not in excluded_characters)
    return ''.join(random.choice(characters) for _ in range(length))

def create_captcha_image(text, width=200, height=60, font_size=36):
    # Create an image with white background
    # Create an image with white background
    image = Image.new('RGBA', (width, height), (255, 255, 255, 255))  # Use RGBA for alpha channel
    draw = ImageDraw.Draw(image)
    
    # Load a font
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except IOError:
        font = ImageFont.load_default()
    
    # Create a temporary image to draw text
    temp_image = Image.new('RGBA', (width, height), (255, 255, 255, 0))  # Transparent background
    temp_draw = ImageDraw.Draw(temp_image)
    
    # Draw the text on the temporary image
    text_width, text_height = temp_draw.textsize(text, font=font)
    text_x = (width - text_width) / 2
    text_y = (height - text_height) / 2
    temp_draw.text((text_x, text_y), text, font=font, fill=(0, 0, 0, 255))  # Black text
    
    # Rotate or skew the text randomly
    angle = random.uniform(-10, 10)  # Random rotation angle between -20 and 20 degrees
    rotated_image = temp_image.rotate(angle, expand=True)
    
    # Convert rotated image to RGBA to ensure transparency
    rotated_image = rotated_image.convert('RGBA')
    
    # Paste the rotated image onto the main image with some random offset
    
    image.paste(rotated_image, (0,-20), rotated_image)  # Use rotated_image as mask

    # Draw horizontal lines
    num_lines = random.randint(2, 4)  # Random number of lines
    for _ in range(num_lines):
        line_y = random.randint(10, height - 10)
        line_thickness = random.randint(2, 3)  # Random line thickness
        draw.line([(0, line_y), (width, line_y)], fill=(0, 0, 0, 100), width=line_thickness)
    
    # Optionally add noise
    for _ in range(100):
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        draw.point((x, y), fill=(0, 0, 0))
    
    # Save image to a BytesIO object
    buffer = BytesIO()
    image.save(buffer, format='PNG')
    buffer.seek(0)
    return buffer

def captcha_image(request):
    # Generate random CAPTCHA text
    captcha_text = generate_captcha_text()
    
    # Create CAPTCHA image
    image_buffer = create_captcha_image(captcha_text)
    
    # Return the image as a response
    response = HttpResponse(image_buffer, content_type='image/png')
    
    # Optionally, store the CAPTCHA text in the session or elsewhere
    request.session['captcha_text'] = captcha_text
    
    return response


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

    return render(request,'trekkapp/main.html', {"name":"Monsson", "trekking":Trekking.objects.all(),"cities":City.objects.all(),"festival":Festival.objects.all(),"adventure":Adventure.objects.all(), "camping":Camping.objects.all(),"cycling":Cycling.objects.all(), "tours":Tours.objects.all(),"cities_json":json.dumps(list(City.objects.all().values('name'))),"marquee":Marquee.objects.first() })

def trekking(request):

    return render(request,'trekkapp/trekking.html', {"name":"Monsson", "trekking":Trekking.objects.all(),"cities":City.objects.all(),"festival":Festival.objects.all(),"adventure":Adventure.objects.all(), "camping":Camping.objects.all(),"cycling":Cycling.objects.all(), "tours":Tours.objects.all(),"cities_json":json.dumps(list(City.objects.all().values('name'))),"marquee":Marquee.objects.first() })

def festivals(request):

    return render(request,'trekkapp/festival.html', {"name":"Monsson", "trekking":Trekking.objects.all(),"cities":City.objects.all(),"festival":Festival.objects.all(),"adventure":Adventure.objects.all(), "camping":Camping.objects.all(),"cycling":Cycling.objects.all(), "tours":Tours.objects.all(),"cities_json":json.dumps(list(City.objects.all().values('name'))),"marquee":Marquee.objects.first() })

def adventure(request):

    return render(request,'trekkapp/adventure.html', {"name":"Monsson", "trekking":Trekking.objects.all(),"cities":City.objects.all(),"festival":Festival.objects.all(),"adventure":Adventure.objects.all(), "camping":Camping.objects.all(),"cycling":Cycling.objects.all(), "tours":Tours.objects.all(),"cities_json":json.dumps(list(City.objects.all().values('name'))),"marquee":Marquee.objects.first() })

def cycling(request):

    return render(request,'trekkapp/cycling.html', {"name":"Monsson", "trekking":Trekking.objects.all(),"cities":City.objects.all(),"festival":Festival.objects.all(),"adventure":Adventure.objects.all(), "camping":Camping.objects.all(),"cycling":Cycling.objects.all(), "tours":Tours.objects.all(),"cities_json":json.dumps(list(City.objects.all().values('name'))),"marquee":Marquee.objects.first() })

def camping(request):

    return render(request,'trekkapp/camping.html', {"name":"Monsson", "trekking":Trekking.objects.all(),"cities":City.objects.all(),"festival":Festival.objects.all(),"adventure":Adventure.objects.all(), "camping":Camping.objects.all(),"cycling":Cycling.objects.all(), "tours":Tours.objects.all(),"cities_json":json.dumps(list(City.objects.all().values('name'))),"marquee":Marquee.objects.first() })

def tour(request):

    return render(request,'trekkapp/tours.html', {"name":"Monsson", "trekking":Trekking.objects.all(),"cities":City.objects.all(),"festival":Festival.objects.all(),"adventure":Adventure.objects.all(), "camping":Camping.objects.all(),"cycling":Cycling.objects.all(), "tours":Tours.objects.all(),"cities_json":json.dumps(list(City.objects.all().values('name'))),"marquee":Marquee.objects.first() })

def about(request):
    return render(request,'trekkapp/About.html')

def terms(request):

    return render(request,'trekkapp/terms.html', {"name":"Monsson", "trekking":Trekking.objects.all(),"cities":City.objects.all(),"festival":Festival.objects.all(),"adventure":Adventure.objects.all(), "camping":Camping.objects.all(),"cycling":Cycling.objects.all(), "tours":Tours.objects.all(),"cities_json":json.dumps(list(City.objects.all().values('name'))),"marquee":Marquee.objects.first() })

def company(request):

    return render(request,'trekkapp/company.html', {"name":"Monsson", "trekking":Trekking.objects.all(),"cities":City.objects.all(),"festival":Festival.objects.all(),"adventure":Adventure.objects.all(), "camping":Camping.objects.all(),"cycling":Cycling.objects.all(), "tours":Tours.objects.all(),"cities_json":json.dumps(list(City.objects.all().values('name'))),"marquee":Marquee.objects.first() })
def consent(request):

    return render(request,'trekkapp/consent.html', {"name":"Monsson", "trekking":Trekking.objects.all(),"cities":City.objects.all(),"festival":Festival.objects.all(),"adventure":Adventure.objects.all(), "camping":Camping.objects.all(),"cycling":Cycling.objects.all(), "tours":Tours.objects.all(),"cities_json":json.dumps(list(City.objects.all().values('name'))),"marquee":Marquee.objects.first() })

def client(request):

    return render(request,'trekkapp/client.html', {"name":"Monsson", "trekking":Trekking.objects.all(),"cities":City.objects.all(),"festival":Festival.objects.all(),"adventure":Adventure.objects.all(), "camping":Camping.objects.all(),"cycling":Cycling.objects.all(), "tours":Tours.objects.all(),"cities_json":json.dumps(list(City.objects.all().values('name'))),"marquee":Marquee.objects.first() })

def enviroment(request):

    return render(request,'trekkapp/enviroment.html', {"name":"Monsson", "trekking":Trekking.objects.all(),"cities":City.objects.all(),"festival":Festival.objects.all(),"adventure":Adventure.objects.all(), "camping":Camping.objects.all(),"cycling":Cycling.objects.all(), "tours":Tours.objects.all(),"cities_json":json.dumps(list(City.objects.all().values('name'))),"marquee":Marquee.objects.first() })
def paymentoptions(request):

    return render(request,'trekkapp/paymentoptions.html', {"name":"Monsson", "trekking":Trekking.objects.all(),"cities":City.objects.all(),"festival":Festival.objects.all(),"adventure":Adventure.objects.all(), "camping":Camping.objects.all(),"cycling":Cycling.objects.all(), "tours":Tours.objects.all(),"cities_json":json.dumps(list(City.objects.all().values('name'))),"marquee":Marquee.objects.first() })
def privacy(request):

    return render(request,'trekkapp/privacy.html', {"name":"Monsson", "trekking":Trekking.objects.all(),"cities":City.objects.all(),"festival":Festival.objects.all(),"adventure":Adventure.objects.all(), "camping":Camping.objects.all(),"cycling":Cycling.objects.all(), "tours":Tours.objects.all(),"cities_json":json.dumps(list(City.objects.all().values('name'))),"marquee":Marquee.objects.first() })
def refund(request):

    return render(request,'trekkapp/refund.html', {"name":"Monsson", "trekking":Trekking.objects.all(),"cities":City.objects.all(),"festival":Festival.objects.all(),"adventure":Adventure.objects.all(), "camping":Camping.objects.all(),"cycling":Cycling.objects.all(), "tours":Tours.objects.all(),"cities_json":json.dumps(list(City.objects.all().values('name'))),"marquee":Marquee.objects.first() })
def registration(request):

    return render(request,'trekkapp/registration.html', {"name":"Monsson", "trekking":Trekking.objects.all(),"cities":City.objects.all(),"festival":Festival.objects.all(),"adventure":Adventure.objects.all(), "camping":Camping.objects.all(),"cycling":Cycling.objects.all(), "tours":Tours.objects.all(),"cities_json":json.dumps(list(City.objects.all().values('name'))),"marquee":Marquee.objects.first() })
def social(request):

    return render(request,'trekkapp/social.html', {"name":"Monsson", "trekking":Trekking.objects.all(),"cities":City.objects.all(),"festival":Festival.objects.all(),"adventure":Adventure.objects.all(), "camping":Camping.objects.all(),"cycling":Cycling.objects.all(), "tours":Tours.objects.all(),"cities_json":json.dumps(list(City.objects.all().values('name'))),"marquee":Marquee.objects.first() })
def team(request):

    return render(request,'trekkapp/team.html', {"name":"Monsson", "trekking":Trekking.objects.all(),"cities":City.objects.all(),"festival":Festival.objects.all(),"adventure":Adventure.objects.all(), "camping":Camping.objects.all(),"cycling":Cycling.objects.all(), "tours":Tours.objects.all(),"cities_json":json.dumps(list(City.objects.all().values('name'))),"marquee":Marquee.objects.first() })
def testimonials(request):

    return render(request,'trekkapp/testimonials.html', {"name":"Monsson", "trekking":Trekking.objects.all(),"cities":City.objects.all(),"festival":Festival.objects.all(),"adventure":Adventure.objects.all(), "camping":Camping.objects.all(),"cycling":Cycling.objects.all(), "tours":Tours.objects.all(),"cities_json":json.dumps(list(City.objects.all().values('name'))),"marquee":Marquee.objects.first() })
def useragreement(request):

    return render(request,'trekkapp/useragreement.html', {"name":"Monsson", "trekking":Trekking.objects.all(),"cities":City.objects.all(),"festival":Festival.objects.all(),"adventure":Adventure.objects.all(), "camping":Camping.objects.all(),"cycling":Cycling.objects.all(), "tours":Tours.objects.all(),"cities_json":json.dumps(list(City.objects.all().values('name'))),"marquee":Marquee.objects.first() })


class Detailedtrek(DetailView):
    model=City
    template_name="trekkapp/trekdetails.html"

    def get_context_data(self, **kwargs):
        context = super(Detailedtrek,self).get_context_data(**kwargs)
        context["cities"]=City.objects.all()
        context["Gallery"]=Gallery.objects.all().filter(city=self.get_object())
        context["cities_json"]=json.dumps(list(City.objects.all().values('name')))
        context["marquee"]=Marquee.objects.first()
        self.object=self.get_object()
        print(self.object.trekking)
        context["form"]=EnquireForm(initial={'thetrek':self.object.__dict__})
        return context
    
    def post(self, request, **kwargs):
        print(request.POST)
        if 'name' in request.POST:
            recaptcha_response = request.POST.get('g-recaptcha-response')
            if verify_recaptcha(recaptcha_response):
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
                    return render(request, 'trekkapp/contact.html', {'form': form, "cities_json":json.dumps(list(City.objects.all().values('name'))),"marquee":Marquee.objects.first()})
        elif 'captchasubmit' in request.POST:
            print("it works")
            user_input = request.POST.get('captcha')
            captcha_text = request.session.get('captcha_text')
            print(request.POST.get('captcha'))
            print(request.session)
            if user_input == captcha_text:
                print("hi")
                return HttpResponseRedirect(self.request.path_info)
            else:
                return render(request, 'trekkapp/contact.html', {'form': EnquireForm, "cities_json":json.dumps(list(City.objects.all().values('name'))),"marquee":Marquee.objects.first()})
        else:
             return render(request, 'trekkapp/contact.html', {'form': EnquireForm, "cities_json":json.dumps(list(City.objects.all().values('name'))),"marquee":Marquee.objects.first()})
class DetailedCycle(DetailView):
    model=Cycling
    template_name="trekkapp/trekdetails.html"

    def get_context_data(self, **kwargs):
        context = super(DetailedCycle,self).get_context_data(**kwargs)
        context["cities"]=City.objects.all()
        context["Gallery"]=Gallery.objects.all().filter(cycling=self.get_object())
        context["cities_json"]=json.dumps(list(City.objects.all().values('name')))
        context["form"]=EnquireForm(initial={'thetrek':self.object})
        context["marquee"]=Marquee.objects.first()
        return context
    
    
    def post(self, request, **kwargs):
        print(request.POST)
        if 'name' in request.POST:
            recaptcha_response = request.POST.get('g-recaptcha-response')
            if verify_recaptcha(recaptcha_response):
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
                    return render(request, 'trekkapp/contact.html', {'form': form, "cities_json":json.dumps(list(City.objects.all().values('name'))),"marquee":Marquee.objects.first()})
        elif 'captchasubmit' in request.POST:
            print("it works")
            user_input = request.POST.get('captcha')
            captcha_text = request.session.get('captcha_text')
        
            if user_input == captcha_text:
                print("hi")
                return HttpResponseRedirect(self.request.path_info)
        else:
             return render(request, 'trekkapp/contact.html', {'form': EnquireForm, "cities_json":json.dumps(list(City.objects.all().values('name'))),"marquee":Marquee.objects.first()})
class DetailedCamp(DetailView):
    model=Camping
    template_name="trekkapp/trekdetails.html"

    def get_context_data(self, **kwargs):
        context = super(DetailedCamp,self).get_context_data(**kwargs)
        context["cities"]=City.objects.all()
        context["Gallery"]=Gallery.objects.all().filter(camping=self.get_object())
        context["cities_json"]=json.dumps(list(City.objects.all().values('name')))
        context["form"]=EnquireForm(initial={'thetrek':self.object})
        context["marquee"]=Marquee.objects.first()
        return context
    def post(self, request, **kwargs):
        print(request.POST)
        if 'name' in request.POST:
            recaptcha_response = request.POST.get('g-recaptcha-response')
            if verify_recaptcha(recaptcha_response):
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
                    return render(request, 'trekkapp/contact.html', {'form': form, "cities_json":json.dumps(list(City.objects.all().values('name'))),"marquee":Marquee.objects.first()})
        elif 'something' in request.POST:
            user_input = request.POST.get('captcha')
            captcha_text = request.session.get('captcha_text')
        
            if user_input == captcha_text:
                print("hi")
                return HttpResponseRedirect(self.request.path_info)
        else:
             return render(request, 'trekkapp/contact.html', {'form': EnquireForm, "cities_json":json.dumps(list(City.objects.all().values('name'))),"marquee":Marquee.objects.first()})
class Detailedtour(DetailView):
    model=Tours
    template_name="trekkapp/trekdetails.html"

    def get_context_data(self, **kwargs):
        context = super(Detailedtour,self).get_context_data(**kwargs)
        context["cities"]=City.objects.all()
        context["Gallery"]=Gallery.objects.all().filter(tours=self.get_object())
        context["cities_json"]=json.dumps(list(City.objects.all().values('name')))
        context["form"]=EnquireForm(initial={'thetrek':self.object})
        context["marquee"]=Marquee.objects.first()
        return context
    
    def post(self, request, **kwargs):
        print(request.POST)
        if 'name' in request.POST:
            recaptcha_response = request.POST.get('g-recaptcha-response')
            if verify_recaptcha(recaptcha_response):
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
                    return render(request, 'trekkapp/contact.html', {'form': form, "cities_json":json.dumps(list(City.objects.all().values('name'))),"marquee":Marquee.objects.first()})
        elif 'something' in request.POST:
            user_input = request.POST.get('captcha')
            captcha_text = request.session.get('captcha_text')
        
            if user_input == captcha_text:
                print("hi")
                return HttpResponseRedirect(self.request.path_info)

        else:
             return render(request, 'trekkapp/contact.html', {'form': EnquireForm, "cities_json":json.dumps(list(City.objects.all().values('name'))),"marquee":Marquee.objects.first()})
        
def contact(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        recaptcha_response = request.POST.get('g-recaptcha-response')
        if verify_recaptcha(recaptcha_response):
            print("ysy")
            if form.is_valid():
                form.save()
                recipient_email = 'jaideep.technographix@gmail.com'
                subject = 'the trekers contact'
                message = f"Name: {form.cleaned_data['name']}\nEmail: {form.cleaned_data['email']}\nMessage: {form.cleaned_data['message']}\nNumber: {form.cleaned_data['number']}"
                from_email = form.cleaned_data['email']  # Replace with your email address

                # Send email
                send_mail(subject, message, from_email, [recipient_email])
                return render(request,'trekkapp/contact.html',{'form':ContactForm,'success':True, "cities_json":json.dumps(list(City.objects.all().values('name'))),"marquee":Marquee.objects.first()})
            else:
                pattern=r"^(?:\+91|91)?[789]\d{9}$"
                emailpattern=r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$"
                if(re.match(pattern,request.POST['number'])==None):
                    return render(request,'trekkapp/contact.html',{'form':ContactForm,'number':True, "cities_json":json.dumps(list(City.objects.all().values('name'))),"marquee":Marquee.objects.first()})
                elif(re.match(emailpattern,request.POST['email'])==None):
                    return render(request,'trekkapp/contact.html',{'form':ContactForm,'email':True, "cities_json":json.dumps(list(City.objects.all().values('name'))),"marquee":Marquee.objects.first()})
                else:
                    return render(request,'trekkapp/contact.html',{'form':ContactForm,'failure':True, "cities_json":json.dumps(list(City.objects.all().values('name'))),"marquee":Marquee.objects.first()})
        else:
            return render(request,'trekkapp/contact.html',{'form':ContactForm,'captcha':True, "cities_json":json.dumps(list(City.objects.all().values('name'))),"marquee":Marquee.objects.first()})
    else:
        return render(request,'trekkapp/contact.html',{'form':ContactForm, "cities_json":json.dumps(list(City.objects.all().values('name'))),"marquee":Marquee.objects.first()})

def personal(request):
    if request.method=='POST':
        form=PersonalForm(request.POST)
        recaptcha_response = request.POST.get('g-recaptcha-response')
        if verify_recaptcha(recaptcha_response):
            if form.is_valid():
                name = request.POST.get('name')
                email = request.POST.get('email')
                number = request.POST.get('number')
                date_str = request.POST.get('date')
                message = request.POST.get('message')

                # Parse the date field
                if date_str:
                    try:
                        event_date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
                    except ValueError:
                        event_date = timezone.now().date()
                else:
                    event_date = timezone.now().date()

                # Create and save the new PersonalTrek instance
                personal_trek = personaltrek(
                    name=name,
                    email=email,
                    number=number,
                    date=event_date,
                    message=message
                )
                personal_trek.save()
                recipient_email = 'jaideep.technographix@gmail.com'
                subject = 'the trekers custom trek'
                message = f"Name: {form.cleaned_data['name']}\nEmail: {form.cleaned_data['email']}\nMessage: {form.cleaned_data['message']}\nNumber: {form.cleaned_data['number']}"
                from_email = form.cleaned_data['email']  # Replace with your email address

                # Send email
                send_mail(subject, message, from_email, [recipient_email])
                return render(request,'trekkapp/contact.html',{'form':PersonalForm,"personal":True,"trekking":Trekking.objects.all(),"cities":City.objects.all(),"festival":Festival.objects.all(),"adventure":Adventure.objects.all(), "camping":Camping.objects.all(),"cycling":Cycling.objects.all(), "tours":Tours.objects.all(),'success':True, "cities_json":json.dumps(list(City.objects.all().values('name'))),"marquee":Marquee.objects.first()})
            else:
                pattern=r"^(?:\+91|91)?[789]\d{9}$"
                emailpattern=r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$"
                if(re.match(pattern,request.POST['number'])==None):
                    return render(request,'trekkapp/contact.html',{'form':PersonalForm,"personal":True,"trekking":Trekking.objects.all(),"cities":City.objects.all(),"festival":Festival.objects.all(),"adventure":Adventure.objects.all(), "camping":Camping.objects.all(),"cycling":Cycling.objects.all(), "tours":Tours.objects.all(),'number':True, "cities_json":json.dumps(list(City.objects.all().values('name'))),"marquee":Marquee.objects.first()})
                elif(re.match(emailpattern,request.POST['email'])==None):
                    return render(request,'trekkapp/contact.html',{'form':PersonalForm,"personal":True,"trekking":Trekking.objects.all(),"cities":City.objects.all(),"festival":Festival.objects.all(),"adventure":Adventure.objects.all(), "camping":Camping.objects.all(),"cycling":Cycling.objects.all(), "tours":Tours.objects.all(),'email':True, "cities_json":json.dumps(list(City.objects.all().values('name'))),"marquee":Marquee.objects.first()})
                else:
                    return render(request,'trekkapp/contact.html',{'form':PersonalForm,"personal":True,"trekking":Trekking.objects.all(),"cities":City.objects.all(),"festival":Festival.objects.all(),"adventure":Adventure.objects.all(), "camping":Camping.objects.all(),"cycling":Cycling.objects.all(), "tours":Tours.objects.all(),'failure':True, "cities_json":json.dumps(list(City.objects.all().values('name'))),"marquee":Marquee.objects.first()})
        else:
            return render(request,'trekkapp/contact.html',{'form':PersonalForm,"personal":True,"trekking":Trekking.objects.all(),"cities":City.objects.all(),"festival":Festival.objects.all(),"adventure":Adventure.objects.all(), "camping":Camping.objects.all(),"cycling":Cycling.objects.all(), "tours":Tours.objects.all(),'captcha':True, "cities_json":json.dumps(list(City.objects.all().values('name'))),"marquee":Marquee.objects.first()})
    else:
        return render(request,'trekkapp/contact.html',{'form':PersonalForm,"personal":True,"trekking":Trekking.objects.all(),"cities":City.objects.all(),"festival":Festival.objects.all(),"adventure":Adventure.objects.all(), "camping":Camping.objects.all(),"cycling":Cycling.objects.all(), "tours":Tours.objects.all(), "cities_json":json.dumps(list(City.objects.all().values('name'))),"marquee":Marquee.objects.first()})

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
def is_ajax(request):
    return request.headers.get('x-requested-with') == 'XMLHttpRequest'

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
        print("hi")
        if form.is_valid():
            form.save(commit=False)
            form.article=self.object
            form.save()
            return HttpResponseRedirect(self.request.path_info)
            
        elif is_ajax(request):
            model_id = self.kwargs['pk']  # Assuming your model uses pk as the primary key
            model = self.get_object()
            print("ajax")
            action = request.POST.get('action')
            # Logic to update the likes of the model
            # Example:
            if action == 'like':
                print("yo")
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
