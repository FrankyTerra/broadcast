from core.api.broadcast.serializers import BroadcastSerializer
from core.api.views import CustomModelViewSet
from core.models import Broadcast


class BroadcastViewSet(CustomModelViewSet):
    """
    Набор представлений Трансляций
    """

    queryset = Broadcast.objects.all()
    serializer_class = BroadcastSerializer
