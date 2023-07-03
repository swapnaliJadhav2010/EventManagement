from django.urls import path
from .views import SportListCreateAPIView, EventListCreateAPIView, SelectionListCreateAPIView

urlpatterns = [
    path('sports/', SportListCreateAPIView.as_view(), name='sport-list-create'),
    path('events/', EventListCreateAPIView.as_view(), name='event-list-create'),
    path('selections/', SelectionListCreateAPIView.as_view(), name='selection-list-create'),
]
