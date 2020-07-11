from core.api.comment.serializers import CommentSerializer
from core.api.views import CustomModelViewSet
from core.models import Comment


class CommentViewSet(CustomModelViewSet):
    """
    Набор представлений комментариев
    """

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
