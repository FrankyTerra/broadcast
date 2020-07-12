from core.api.event.permissions import EventAccessPolicy
from core.api.event.serializers import EventSerializer, EventCreateUpdateSerializer
from core.api.views import CustomModelViewSet
from core.models import Event


class EventViewSet(CustomModelViewSet):
    """
    Набор представлений Событий
    """

    queryset = Event.objects.all()
    serializer_class = EventSerializer
    serializer_map = {
        'create': EventCreateUpdateSerializer,
        'update': EventCreateUpdateSerializer,
    }
    permission_classes = (EventAccessPolicy,)
    filterset_fields = ['broadcast', 'broadcast__event_type', 'date_created']
