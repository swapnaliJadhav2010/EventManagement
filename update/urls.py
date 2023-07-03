from django.urls import path
from .views import SportUpdateView, EventUpdateView, SelectionUpdateView

urlpatterns = [
    path('sports/<int:sport_id>/', SportUpdateView.as_view(), name='sport-list-update'),
    path('events/<int:event_id>/', EventUpdateView.as_view(), name='event-list-update'),
    path('selections/<int:selection_id>/', SelectionUpdateView.as_view(), name='selection-list-update'),
]
