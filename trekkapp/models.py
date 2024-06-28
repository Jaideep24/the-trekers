from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models
from django.utils import timezone


# Create your models here.
class Trekking(models.Model):
    title=models.CharField(max_length=100)

    def __str__(self):
        return self.title
class Festival(models.Model):
    title=models.CharField(max_length=100)

    def __str__(self):
        return self.title
class Adventure(models.Model):
    title=models.CharField(max_length=100)

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
    def __str__(self):
        return self.name
    
class contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    number=models.IntegerField(max_length=10)
    message=models.TextField()
class enquire(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    number=models.IntegerField(max_length=10)
    message=models.TextField()
    thetrek=models.CharField(max_length=100)
class personaltrek(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    number=models.IntegerField(max_length=10)
    message=models.TextField()
