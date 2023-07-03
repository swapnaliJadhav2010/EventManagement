from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from create.models import Sport, Event, Selection
from .serializers import SportSerializer, EventSerializer, SelectionSerializer
from django.utils import timezone

class EventListAPITestCase(APITestCase):
    def setUp(self):
        self.sport = Sport.objects.create(name='Football', slug='FT', active=True)
        self.event1 = Event.objects.create(name='Football Match', slug='FTM', active=True, type='inplay', sport=self.sport, status='Pending', scheduled_start=timezone.make_aware(timezone.datetime(2023, 7, 1, 18, 0, 0)))
        self.event2 = Event.objects.create(name='Football Tounament', slug='FTT', active=True, type='inplay', sport=self.sport, status='Pending', scheduled_start=timezone.make_aware(timezone.datetime(2023, 7, 1, 18, 0, 0)))
        self.event3 = Event.objects.create(name='Football fest', slug='FTF', active=True, type='inplay', sport=self.sport, status='Pending', scheduled_start=timezone.make_aware(timezone.datetime(2023, 7, 1, 18, 0, 0)))

    def test_event_list_filter_by_sport_name(self):
        url = reverse('event-list')
        sport_name = 'Football'
        response = self.client.get(url, {'sport_name': sport_name})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)
        self.assertEqual(response.data[0]['sport']['name'], sport_name)
        self.assertEqual(response.data[1]['sport']['name'], sport_name)
        self.assertEqual(response.data[2]['sport']['name'], sport_name)

class SelectionListAPITestCase(APITestCase):
    def setUp(self):
        self.sport = Sport.objects.create(name='Football', slug='FT', active=True)
        self.event = Event.objects.create(name='Football Match', slug='FTM', active=True, type='inplay', sport=self.sport, status='Pending', scheduled_start=timezone.make_aware(timezone.datetime(2023, 7, 1, 18, 0, 0)))
        self.selection1 = Selection.objects.create(name='Child', event=self.event, price='10.00', active=True, outcome='Win')
        self.selection2 = Selection.objects.create(name='Adult', event=self.event, price='20.00', active=True, outcome='Loss')

    def test_selection_list_filter_by_event_name_and_price_range(self):
        url = reverse('selection-list')
        event_name = 'Football Match'
        min_price = '5.00'
        max_price = '15.00'
        response = self.client.get(url, {'event_name': event_name, 'min_price': min_price, 'max_price': max_price})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['event']['name'], event_name)
        self.assertLessEqual(float(response.data[0]['price']), float(max_price))
        self.assertGreaterEqual(float(response.data[0]['price']), float(min_price))
