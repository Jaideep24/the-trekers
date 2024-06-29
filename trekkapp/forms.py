from django import forms
from .models import *

class ContactForm(forms.ModelForm):
    class Meta:
        model=contact
        fields=['name','email','number','message']

class EnquireForm(forms.ModelForm):
    thetrek=forms.CharField(required=False)
    class Meta:
        model=enquire
        fields=['name','email','number','message','thetrek']
        widgets={'thetrek':forms.HiddenInput()}

class PersonalForm(forms.ModelForm):
    class Meta:
        model=personaltrek
        fields=['name','email','number','message']