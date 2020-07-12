from rest_framework import serializers, fields

from user.models import User


class UserRetrieveSerializer(serializers.ModelSerializer):
    """
    Сериализатор пользователя
    """

    role_display = fields.ReadOnlyField(source='get_role_display')

    class Meta:
        model = User
        fields = ('id', 'comment_author_name', 'role_display')


