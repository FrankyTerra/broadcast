from rest_framework import serializers

from core.api.broadcast.serializers import BroadcastSerializer
from core.models import Comment
from user.api.serializers import UserRetrieveSerializer


class BaseCommentSerializer(serializers.ModelSerializer):
    """
    Сериализатор Комментария
    """

    class Meta:
        model = Comment
        fields = ('id', 'user', 'broadcast', 'text', 'date_created')


class CommentSerializer(BaseCommentSerializer):
    """
    Сериализатор Комментария
    """

    broadcast = BroadcastSerializer(read_only=True)
    user = UserRetrieveSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'user', 'broadcast', 'text', 'date_created')


class CommentCreateSerializer(BaseCommentSerializer):
    """
    Сериализатор добавления Комментария
    """

    class Meta:
        model = Comment
        fields = ('id', 'user', 'broadcast', 'text')
