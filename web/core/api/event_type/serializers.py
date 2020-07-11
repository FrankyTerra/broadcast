from rest_framework import serializers

from core.models import EventType


class EventTypeSerializer(serializers.ModelSerializer):
    """
    Сериализатор Типа события
    """

    class Meta:
        model = EventType
        fields = ('id', 'name', 'description')
