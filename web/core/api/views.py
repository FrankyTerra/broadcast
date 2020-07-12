from django.conf import settings
from rest_framework import mixins
from rest_framework.generics import RetrieveAPIView, GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from typing import Dict
from rest_framework.serializers import Serializer


class ViewSetMixin:
    """
    Миксин представлений
    """

    http_method_names = settings.ALLOWED_HTTP_METHOD_NAMES
    permission_classes = (IsAuthenticated,)


class MultiSerializerViewSetMixin:
    """
    Миксин мульти сериализаторов
    """

    serializer_map: Dict[str, Serializer] = {}

    def get_serializer_class(self):
        try:
            return self.serializer_map[self.action]
        except (KeyError, AttributeError):
            return super().get_serializer_class()


class CustomModelViewSet(ViewSetMixin, MultiSerializerViewSetMixin, ModelViewSet):
    """
    Кастомный набор модельных представлений
    """

    pass


class CustomRetrieveAPIView(ViewSetMixin, RetrieveAPIView):
    """
    Кастомное представление информации об объекте
    """

    pass
