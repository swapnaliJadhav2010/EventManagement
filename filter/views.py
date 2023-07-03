from rest_framework import generics
from create.models import Sport, Event,Selection
from .serializers import SportSerializer, EventSerializer, SelectionSerializer

class SportListAPIView(generics.ListAPIView):
    queryset = Sport.objects.all()
    serializer_class = SportSerializer

class EventListAPIView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        sport_name = self.request.query_params.get('sport_name')
        if sport_name:
            queryset = queryset.filter(sport__name=sport_name)
        return queryset

class SelectionListAPIView(generics.ListAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        event_name = self.request.query_params.get('event_name')
        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')

        if event_name:
            queryset = queryset.filter(event__name=event_name)

        if min_price and max_price:
            queryset = queryset.filter(price__gte=min_price, price__lte=max_price)
        elif min_price:
            queryset = queryset.filter(price__gte=min_price)
        elif max_price:
            queryset = queryset.filter(price__lte=max_price)

        return queryset