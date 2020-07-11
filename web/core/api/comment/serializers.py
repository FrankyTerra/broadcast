from rest_framework import serializers

from core.api.broadcast.serializers import BroadcastSerializer
from core.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    """
    Сериализатор Комментария
    """

    broadcast = BroadcastSerializer()

    class Meta:
        model = Comment
        fields = ('id', 'user', 'broadcast', 'text', 'date_created')
