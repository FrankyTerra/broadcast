from rest_framework.generics import ListAPIView

from core.api.event_type.permissions import EventTypeAccessPolicy, EventTypeChoiceAccessPolicy
from core.api.event_type.serializers import EventTypeSerializer, EventTypeChoiceSerializer
from core.api.views import CustomModelViewSet
from core.models import EventType
from rest_framework import filters


class EventTypeViewMixin:
    """
    Миксин представлений типов событий
    """

    queryset = EventType.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class EventTypeViewSet(EventTypeViewMixin, CustomModelViewSet):
    """
    Набор представлений Типа событий
    """

    serializer_class = EventTypeSerializer
    permission_classes = (EventTypeAccessPolicy,)


class EventTypeChoiceView(EventTypeViewMixin, ListAPIView):
    """
    Чейсы для типов событий
    """

    serializer_class = EventTypeChoiceSerializer
    permission_classes = (EventTypeChoiceAccessPolicy,)
    pagination_class = None
