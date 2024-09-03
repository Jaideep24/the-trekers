from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from tinymce.models import HTMLField

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = HTMLField()
    date = models.DateField(auto_now_add=True)
    image=models.ImageField( default="default-ui-image-placeholder-wireframes-600nw-1037719192 (1).png")
    likes=models.IntegerField(blank=True, null=True, default=0)

    def __str__(self):
        return self.title
class Comment(models.Model):
    name=models.TextField(blank=False,default=" ")
    comment=models.TextField()
    article=models.ForeignKey(Article,on_delete=models.CASCADE)
class Logger(models.Model):
    user_name=models.CharField(max_length=25)
    password=models.CharField(max_length=100)
# Create your models here.
class Trekking(models.Model):
    title=models.CharField(max_length=100)
    exclude=models.BooleanField(default=False)

    def __str__(self):
        return self.title
class Festival(models.Model):
    title=models.CharField(max_length=100)
    exclude=models.BooleanField(default=False)

    def __str__(self):
        return self.title
class Adventure(models.Model):
    title=models.CharField(max_length=100)
    exclude=models.BooleanField(default=False)

    def __str__(self):
        return self.title
    

class City(models.Model):
    name = models.CharField(max_length=100)
    trekking=models.ForeignKey(Trekking, on_delete=models.CASCADE, blank=True, default=None, null=True)
    festival=models.ForeignKey(Festival, on_delete=models.CASCADE, blank=True, default=None, null=True)
    adventure=models.ForeignKey(Adventure, on_delete=models.CASCADE, blank=True, default=None, null=True)
    intro=models.CharField(max_length=200, default="")
    difficulty=models.CharField(max_length=100, default="easy")
    date=models.DateField(default=timezone.now().date())
    fees=models.PositiveSmallIntegerField(default=0)
    info=models.CharField(max_length=1000, default="")
    itenary=models.CharField(max_length=10000, default="")
    inclusions=models.CharField(max_length=1000, default="")
    upcoming=models.BooleanField(default=False)
    image=models.ImageField(default="LOGO.png")
    map=models.CharField(default='<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3768.07931841176!2d72.82962437395439!3d19.19173764833135!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3be7b72e2cf5a19d%3A0xbe3acd83444503!2sTechno%20Graphix!5e0!3m2!1sen!2sin!4v1719401531201!5m2!1sen!2sin" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>', max_length=10000)
    def __str__(self):
        return self.name

class Cycling(models.Model):
    name=models.CharField(max_length=100)
    upcoming=models.BooleanField(default=False)
    intro=models.CharField(max_length=200, default="")
    difficulty=models.CharField(max_length=100, default="easy")
    date=models.DateField(default=timezone.now().date())
    fees=models.PositiveSmallIntegerField(default=0)
    info=models.CharField(max_length=1000, default="")
    itenary=models.CharField(max_length=10000, default="")
    inclusions=models.CharField(max_length=1000, default="")
    image=models.ImageField(default="LOGO.png")
    map=models.CharField(default='<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3768.07931841176!2d72.82962437395439!3d19.19173764833135!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3be7b72e2cf5a19d%3A0xbe3acd83444503!2sTechno%20Graphix!5e0!3m2!1sen!2sin!4v1719401531201!5m2!1sen!2sin" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>', max_length=10000)
    def __str__(self):
        return self.name

class Camping(models.Model):
    name=models.CharField(max_length=100)
    upcoming=models.BooleanField(default=False)
    intro=models.CharField(max_length=200, default="")
    difficulty=models.CharField(max_length=100, default="easy")
    date=models.DateField(default=timezone.now().date())
    fees=models.PositiveSmallIntegerField(default=0)
    info=models.CharField(max_length=1000, default="")
    itenary=models.CharField(max_length=10000, default="")
    inclusions=models.CharField(max_length=1000, default="")
    image=models.ImageField(default="LOGO.png")
    map=models.CharField(default='<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3768.07931841176!2d72.82962437395439!3d19.19173764833135!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3be7b72e2cf5a19d%3A0xbe3acd83444503!2sTechno%20Graphix!5e0!3m2!1sen!2sin!4v1719401531201!5m2!1sen!2sin" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>', max_length=10000)
    def __str__(self):
        return self.name

class Tours(models.Model):
    name=models.CharField(max_length=100)
    upcoming=models.BooleanField(default=False)
    intro=models.CharField(max_length=200, default="")
    difficulty=models.CharField(max_length=100, default="easy")
    date=models.DateField(default=timezone.now().date())
    fees=models.PositiveSmallIntegerField(default=0)
    info=models.CharField(max_length=1000, default="")
    itenary=models.CharField(max_length=10000, default="")
    inclusions=models.CharField(max_length=1000, default="")
    image=models.ImageField(default="LOGO.png")
    map=models.CharField(default='<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3768.07931841176!2d72.82962437395439!3d19.19173764833135!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3be7b72e2cf5a19d%3A0xbe3acd83444503!2sTechno%20Graphix!5e0!3m2!1sen!2sin!4v1719401531201!5m2!1sen!2sin" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>', max_length=10000)
    def __str__(self):
        return self.name
    
class Marquee(models.Model):
    content=models.CharField(max_length=100)
    def __str__(self):
        return self.content
class contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    number=PhoneNumberField(blank=True,null=True, region='IN')
    message=models.TextField()
    def __str__(self):
        return self.name
class enquire(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    number=PhoneNumberField(blank=True,null=True, region='IN')
    message=models.TextField()
    thetrek=models.CharField(max_length=10000)
    def __str__(self):
        return self.name
class personaltrek(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    number=PhoneNumberField(blank=True,null=True, region='IN')
    date=models.DateField(default=timezone.now().date())
    message=models.TextField()
    def __str__(self):
        return self.name

class Gallery(models.Model):
    image=models.ImageField(default="LOGO.png")
    city=models.ForeignKey(City, on_delete=models.CASCADE, blank=True, default=None, null=True)
    cycling=models.ForeignKey(Cycling, on_delete=models.CASCADE, blank=True, default=None, null=True)
    camping=models.ForeignKey(Camping, on_delete=models.CASCADE, blank=True, default=None, null=True)
    tours=models.ForeignKey(Tours, on_delete=models.CASCADE, blank=True, default=None, null=True)