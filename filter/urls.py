from django.urls import path
from .views import SportListAPIView, EventListAPIView, SelectionListAPIView

urlpatterns = [
    path('sports/', SportListAPIView.as_view(), name='sport-list'),
    path('events/', EventListAPIView.as_view(), name='event-list'),
    path('selections/', SelectionListAPIView.as_view(), name='selection-list'),
]
