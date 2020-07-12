from core.api.broadcast.permissions import BroadcastAccessPolicy
from core.api.broadcast.serializers import BroadcastSerializer, BroadcastCreateUpdateSerializer
from core.api.views import CustomModelViewSet
from core.models import Broadcast


class BroadcastViewSet(CustomModelViewSet):
    """
    Набор представлений Трансляций
    """

    queryset = Broadcast.objects.all()
    serializer_class = BroadcastSerializer
    serializer_map = {
        'create': BroadcastCreateUpdateSerializer,
        'update': BroadcastCreateUpdateSerializer,
    }
    permission_classes = (BroadcastAccessPolicy,)
    filterset_fields = ['date_start', 'event_type']
