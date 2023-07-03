from rest_framework import generics
from .models import Sport, Event, Selection
from .serializers import SportSerializer, EventSerializer, SelectionSerializer

class SportListCreateAPIView(generics.ListCreateAPIView):
    queryset = Sport.objects.all()
    serializer_class = SportSerializer

class EventListCreateAPIView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class SelectionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionSerializer
