from core.api.event.serializers import EventSerializer
from core.api.views import CustomModelViewSet
from core.models import Event


class EventViewSet(CustomModelViewSet):
    """
    Набор представлений Событий
    """

    queryset = Event.objects.all()
    serializer_class = EventSerializer
