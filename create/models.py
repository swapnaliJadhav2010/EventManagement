from django.db import models
from django.utils import timezone

class Sport(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    def update_active_status(self):
        if not self.event_set.filter(active=True).exists():
            self.active = False
        else:
            self.active = True
        self.save()

class Event(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    active = models.BooleanField(default=False)
    type = models.CharField(max_length=10)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    status = models.CharField(max_length=10)
    scheduled_start = models.DateTimeField()
    actual_start = models.DateTimeField(null=True, blank=True)
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.selection_set.filter(active=True).exists():
            self.active = False
        else:
            self.active = True

        self.sport.update_active_status()

        if self.status.lower() == "started" and not self.actual_start:
            self.actual_start = timezone.now()
        elif self.status.lower() != "started" and self.actual_start:
            self.actual_start = None

        super().save(*args, **kwargs)

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
        if not self.event.selection_set.filter(active=True).exists():
            self.event.active = False
        else:
            self.event.active = True

        self.event.sport.update_active_status()

    def __str__(self):
        return self.name
