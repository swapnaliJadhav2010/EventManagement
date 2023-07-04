from django.db import models
from django.utils import timezone

class Sport(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    active = models.BooleanField(default=False)

    def update_activity_status(self):
        if not self.event_set.filter(active=True).exists():
            self.active = False
        else:
            self.active = True
        self.save()

class Event(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    active = models.BooleanField(default=False)
    type = models.CharField(max_length=10)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    status = models.CharField(max_length=10)
    scheduled_start = models.DateTimeField()
    actual_start = models.DateTimeField(null=True, blank=True)

    def update_activity_status(self):
        if not self.selection_set.filter(active=True,outcome='unsettled').exists():
            self.active = False
        else:
            self.active = True
        self.save()
        self.sport.update_activity_status()
    def save(self, *args, **kwargs):
        if self.status == 'started' and not self.actual_start:
            self.actual_start = timezone.now()
        super().save(*args, **kwargs)

class Selection(models.Model):
    name = models.CharField(max_length=50)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    active = models.BooleanField(default=False)
    outcome = models.CharField(max_length=10)
    
    def save(self, *args, **kwargs):
        if self.outcome != 'unsettled':
            self.active = False
        else:
            self.active = True
        super().save(*args, **kwargs)
        self.event.update_activity_status()