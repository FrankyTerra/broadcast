from api.auth.mixins import GetRequestUserAsObjectMixin
from api.auth.serializers import ProfileRetrieveSerializer
from core.api.views import CustomRetrieveAPIView
from user.models import User


class UserProfileRetrieveView(GetRequestUserAsObjectMixin, CustomRetrieveAPIView):
    """
    Представление основной информации профиля пользователя
    """

    queryset = User.objects.all()
    serializer_class = ProfileRetrieveSerializer
