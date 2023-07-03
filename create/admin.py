from django.contrib import admin
from .models import Sport
from .models import Event
from .models import Selection
# Register your models here.

admin.site.register(Sport)
admin.site.register(Event)
admin.site.register(Selection)