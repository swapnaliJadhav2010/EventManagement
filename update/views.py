from rest_framework.views import APIView
from rest_framework.response import Response
from create.models import Sport, Event, Selection
from .serializers import SportSerializer, EventSerializer, SelectionSerializer
from django.utils import timezone

class SportUpdateView(APIView):
    def get_queryset(self):
        return Sport.objects.all()

    def put(self, request, sport_id):
        sport = self.get_queryset().get(id=sport_id)
        serializer = SportSerializer(sport, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

class EventUpdateView(APIView):
    def get_queryset(self):
        return Event.objects.all()

    def put(self, request, event_id):
        event = Event.objects.get(id=event_id)
        serializer = EventSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
class SelectionUpdateView(APIView):
    def get_queryset(self):
        return Selection.objects.all()

    def put(self, request, selection_id):
        selection = self.get_queryset().get(id=selection_id)
        serializer = SelectionSerializer(selection, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)