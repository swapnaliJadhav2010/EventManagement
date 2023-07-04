from django.db import models
from django.utils import timezone

class Sport(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    active = models.BooleanField(default=False)


class Event(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    active = models.BooleanField(default=False)
    type = models.CharField(max_length=10)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    status = models.CharField(max_length=10)
    scheduled_start = models.DateTimeField()
    actual_start = models.DateTimeField(null=True, blank=True)

   
class Selection(models.Model):
    name = models.CharField(max_length=50)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    active = models.BooleanField(default=False)
    outcome = models.CharField(max_length=10)

