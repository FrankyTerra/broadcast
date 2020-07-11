from django.conf import settings
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet


class ViewSetMixin:
    """
    Миксин представлений
    """

    http_method_names = settings.ALLOWED_HTTP_METHOD_NAMES
    permission_classes = (IsAuthenticated,)


class CustomModelViewSet(ViewSetMixin, ModelViewSet):
    """
    Кастомный набор модельных представлений
    """

    pass


class CustomRetrieveAPIView(ViewSetMixin, RetrieveAPIView):
    """
    Кастомное представление информации об объекте
    """

    pass
