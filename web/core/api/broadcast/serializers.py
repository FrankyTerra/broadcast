from rest_framework import serializers

from core.api.event_type.serializers import EventTypeSerializer
from core.models import Broadcast


class BaseBroadcastSerializer(serializers.ModelSerializer):
    """
    Базовый сериализатор трансляции
    """

    class Meta:
        model = Broadcast
        fields = ('id', 'name', 'description', 'date_start', 'original_link', 'event_type')


class BroadcastSerializer(BaseBroadcastSerializer):
    """
    Сериализатор трансляции
    """

    event_type = EventTypeSerializer(read_only=True)


class BroadcastCreateUpdateSerializer(BaseBroadcastSerializer):
    """
    Сериализатор добавления/обновления трансляции
    """

    pass
