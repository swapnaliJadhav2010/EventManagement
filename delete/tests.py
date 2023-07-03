from django.test import TestCase, Client
from django.urls import reverse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils import timezone

from create.models import Sport, Event, Selection


class DeleteSportTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.sport = Sport.objects.create(name='Football', slug='ft', active=True)

    def test_delete_sport(self):
        response = self.client.delete(reverse('delete_sport', args=[self.sport.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'message': 'Sport deleted successfully'})
        self.assertFalse(Sport.objects.filter(id=self.sport.id).exists())


class DeleteEventTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.sport = Sport.objects.create(name='Football', slug='ft', active=True)
        self.event = Event.objects.create(name='Football match', slug='ftm', active=True,
                                          type='inplay', sport=self.sport, status='pending', scheduled_start=timezone.make_aware(timezone.datetime(2023, 7, 1, 18, 0, 0)))

    def test_delete_event(self):
        response = self.client.delete(reverse('delete_event', args=[self.event.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'message': 'Event deleted successfully'})
        self.assertFalse(Event.objects.filter(id=self.event.id).exists())


class DeleteSelectionTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.sport = Sport.objects.create(name='Football', slug='football', active=True)
        self.event = Event.objects.create(name='Football match', slug='ftm', active=True,
                                          type='inplay', sport=self.sport, status='pending', scheduled_start=timezone.make_aware(timezone.datetime(2023, 7, 1, 18, 0, 0)) )
        self.selection = Selection.objects.create(name='Selection 1', event=self.event,
                                                  price=10.0, active=True, outcome='win', )

    def test_delete_selection(self):
        response = self.client.delete(reverse('delete_selection', args=[self.selection.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'message': 'Selection deleted successfully'})
        self.assertFalse(Selection.objects.filter(id=self.selection.id).exists())
