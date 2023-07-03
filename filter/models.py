from django.db import models
from django.utils import timezone

class Sport(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    active = models.BooleanField(default=False)
    def save(self, *args, **kwargs):
        if not self.event_set.filter(active=True).exists():
            self.active = False
        super().save(*args, **kwargs)
    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    active = models.BooleanField(default=False)
    type = models.CharField(max_length=10)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    status = models.CharField(max_length=10)
    scheduled_start = models.DateTimeField()
    actual_start = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.selection_set.filter(active=True).exists():
            self.active = False
        super().save(*args, **kwargs)

    def update_sport_active_status(self):
        if not self.active:
            self.sport.active = False
            self.sport.save()
    def __str__(self):
        return self.name

class Selection(models.Model):
    name = models.CharField(max_length=50)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    active = models.BooleanField(default=False)
    outcome = models.CharField(max_length=10)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.event.update_sport_active_status()

    def __str__(self):
        return self.name

