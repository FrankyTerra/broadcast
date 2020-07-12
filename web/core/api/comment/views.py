from core.api.comment.permissions import CommentAccessPolicy
from core.api.comment.serializers import CommentSerializer, CommentCreateSerializer
from core.api.views import CustomModelViewSet
from core.models import Comment


class CommentViewSet(CustomModelViewSet):
    """
    Набор представлений комментариев
    """

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    serializer_map = {
        'create': CommentCreateSerializer,
    }
    permission_classes = (CommentAccessPolicy,)
    http_method_names = ('get', 'post', 'delete', 'head', 'options', 'trace')
    filterset_fields = ['broadcast', 'broadcast__event_type', 'date_created']
