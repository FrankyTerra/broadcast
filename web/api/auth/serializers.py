from rest_framework import serializers

from user.models import User


class ProfileRetrieveSerializer(serializers.ModelSerializer):
    """
    Сериализатор профиля пользователя
    """

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'middle_name')
