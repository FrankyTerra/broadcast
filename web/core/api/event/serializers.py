from rest_framework import serializers

from core.api.broadcast.serializers import BroadcastSerializer
from core.models import Event


class EventSerializer(serializers.ModelSerializer):
    """
    Сериализатор События
    """

    broadcast = BroadcastSerializer()

    class Meta:
        model = Event
        fields = ('id', 'broadcast', 'text', 'date_created')
