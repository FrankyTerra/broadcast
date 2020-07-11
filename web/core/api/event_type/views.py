from core.api.event_type.serializers import EventTypeSerializer
from core.api.views import CustomModelViewSet
from core.models import EventType


class EventTypeViewSet(CustomModelViewSet):
    """
    Набор представлений Типа событий
    """

    queryset = EventType.objects.all()
    serializer_class = EventTypeSerializer
