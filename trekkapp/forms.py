from django import forms
from .models import *

class ContactForm(forms.ModelForm):
    class Meta:
        model=contact
        fields=['name','email','number','message']

class EnquireForm(forms.ModelForm):
    class Meta:
        model=enquire
        fields=['name','email','number','message','thetrek']
        

class PersonalForm(forms.ModelForm):
    class Meta:
        model=personaltrek
        fields=['name','email','number','message']