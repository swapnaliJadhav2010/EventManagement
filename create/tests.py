from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Sport, Event, Selection
from .serializers import SportSerializer, EventSerializer, SelectionSerializer
from django.utils import timezone

class SportListCreateAPITestCase(APITestCase):
    def test_create_sport(self):
        url = reverse('sport-list-create')
        data = {'name': 'Football', 'slug': 'FT', 'active': True}
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Sport.objects.count(), 1)
        self.assertEqual(response.data, SportSerializer(Sport.objects.first()).data)

class EventListCreateAPITestCase(APITestCase):
    def setUp(self):
        self.sport = Sport.objects.create(name='Football', slug='FT', active=True)

    def test_create_event(self):
        url = reverse('event-list-create')
        data = {
            'name': 'Football Match',
            'slug': 'FTM',
            'active': True,
            'type': 'inplay',
            'sport': self.sport.pk,
            'status': 'Pending',
            'scheduled_start': timezone.make_aware(timezone.datetime(2023, 7, 1, 18, 0, 0))
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Event.objects.count(), 1)
        self.assertEqual(response.data, EventSerializer(Event.objects.first()).data)

class SelectionListCreateAPITestCase(APITestCase):
    def setUp(self):
        self.sport = Sport.objects.create(name='Football', slug='football', active=True)
        self.event = Event.objects.create(
            name='Football Match',
            slug='FTM',
            active=True,
            type='inplay',
            sport=self.sport,
            status='Pending',
            scheduled_start=timezone.make_aware(timezone.datetime(2023, 7, 1, 18, 0, 0))
        )

    def test_create_selection(self):
        url = reverse('selection-list-create')
        data = {'name': 'Child', 'event': self.event.pk, 'price': '10.00', 'active': True, 'outcome': 'Void'}
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Selection.objects.count(), 1)
        self.assertEqual(response.data, SelectionSerializer(Selection.objects.first()).data)
