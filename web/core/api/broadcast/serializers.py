from rest_framework import serializers

from core.api.event_type.serializers import EventTypeSerializer
from core.models import Broadcast


class BroadcastSerializer(serializers.ModelSerializer):
    """
    Сериализатор трансляции
    """

    event_type = EventTypeSerializer()

    class Meta:
        model = Broadcast
        fields = ('id', 'name', 'description', 'date_start', 'original_link', 'event_type')
