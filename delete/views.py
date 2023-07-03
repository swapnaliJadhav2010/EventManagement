from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from create.models import Sport, Event, Selection
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def delete_sport(request, sport_id):
    sport = get_object_or_404(Sport, id=sport_id)
    sport.delete()
    return JsonResponse({'message': 'Sport deleted successfully'})

@csrf_exempt
def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    event.delete()
    return JsonResponse({'message': 'Event deleted successfully'})

@csrf_exempt
def delete_selection(request, selection_id):
    selection = get_object_or_404(Selection, id=selection_id)
    selection.delete()
    return JsonResponse({'message': 'Selection deleted successfully'})
