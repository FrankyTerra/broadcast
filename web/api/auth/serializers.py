from rest_framework import serializers, fields

from user.models import User


class ProfileRetrieveSerializer(serializers.ModelSerializer):
    """
    Сериализатор профиля пользователя
    """

    role_display = fields.ReadOnlyField(source='get_role_display')

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'middle_name', 'role_display')
