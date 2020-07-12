from rest_framework import serializers

from core.api.broadcast.serializers import BroadcastSerializer
from core.models import Event


class BaseEventSerializer(serializers.ModelSerializer):
    """
    Базовый сериализатор События
    """

    class Meta:
        model = Event
        fields = ('id', 'broadcast', 'text', 'date_created')


class EventSerializer(BaseEventSerializer):
    """
    Сериализатор События
    """

    broadcast = BroadcastSerializer(read_only=True)


class EventCreateUpdateSerializer(BaseEventSerializer):
    """
    Сериализатор добавления/обновления События
    """

    pass
