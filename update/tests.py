from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from create.models import Sport, Event, Selection
from .serializers import SportSerializer, EventSerializer, SelectionSerializer
from django.utils import timezone

class SportUpdateViewTestCase(APITestCase):
    def setUp(self):
        self.sport = Sport.objects.create(name='Football', slug='football', active=True)

    def test_update_sport(self):
        url = reverse('sport-list-update', kwargs={'sport_id': self.sport.id})
        data = {'name': 'Soccer', 'slug': 'soccer', 'active': False}
        response = self.client.put(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.sport.refresh_from_db()
        self.assertEqual(self.sport.name, 'Soccer')
        self.assertEqual(self.sport.slug, 'soccer')
        self.assertEqual(self.sport.active, False)

class EventUpdateViewTestCase(APITestCase):
    def setUp(self):
        self.sport = Sport.objects.create(name='Football', slug='football', active=True)
        self.event = Event.objects.create(
            name='Football Match',
            slug='FTM',
            active=True,
            type='inplay',
            sport=self.sport,
            status='Pending',
            scheduled_start=timezone.now()
        )

    def test_update_event(self):
        url = reverse('event-list-update', kwargs={'event_id': self.event.id})
        data = {
            'name': 'Soccer Match',
            'slug': 'soccer-match',
            'active': False,
            'type': 'prematch',
            'status': 'Started',
            'scheduled_start': timezone.now()
        }
        response = self.client.put(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.event.refresh_from_db()
        self.assertEqual(self.event.name, 'Soccer Match')
        self.assertEqual(self.event.slug, 'soccer-match')
        self.assertEqual(self.event.active, False)
        self.assertEqual(self.event.type, 'prematch')
        self.assertEqual(self.event.status, 'Started')

class SelectionUpdateViewTestCase(APITestCase):
    def setUp(self):
        self.sport = Sport.objects.create(name='Football', slug='football', active=True)
        self.event = Event.objects.create(
            name='Football Match',
            slug='FTM',
            active=True,
            type='inplay',
            sport=self.sport,
            status='Pending',
            scheduled_start=timezone.now()
        )
        self.selection = Selection.objects.create(
            name='Selection 1',
            event=self.event,
            price='10.00',
            active=True,
            outcome='Win'
        )

    def test_update_selection(self):
        url = reverse('selection-list-update', kwargs={'selection_id': self.selection.id})
        data = {'name': 'Updated Selection', 'price': '20.00', 'active': False, 'outcome': 'Lose'}
        response = self.client.put(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.selection.refresh_from_db()
        self.assertEqual(self.selection.name, 'Updated Selection')
        self.assertEqual(str(self.selection.price), '20.00')
        self.assertEqual(self.selection.active, False)
        self.assertEqual(self.selection.outcome, 'Lose')
