from django.urls import path

from .views import delete_sport, delete_event, delete_selection

app_name = 'delete'

urlpatterns = [
    path('sport/<int:sport_id>/', delete_sport, name='delete_sport'),
    path('event/<int:event_id>/', delete_event, name='delete_event'),
    path('selection/<int:selection_id>/', delete_selection, name='delete_selection'),
]
