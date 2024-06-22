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
    info=models.CharField(max_length=100, default="")
    itenary=models.CharField(max_length=100, default="")
    inclusions=models.CharField(max_length=100, default="")
    def __str__(self):
        return self.name

class Cycling(models.Model):
    name=models.CharField(max_length=100)

class Camping(models.Model):
    name=models.CharField(max_length=100)

class Tours(models.Model):
    name=models.CharField(max_length=100)
