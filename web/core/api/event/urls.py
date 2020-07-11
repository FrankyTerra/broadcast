from django.urls import path, include

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from rest_framework.permissions import IsAdminUser
from rest_framework.routers import SimpleRouter

from core.api.event.views import EventViewSet

app_name = 'event'

schema_view = get_schema_view(
    openapi.Info(
        title="Трансляции. API Событий",
        default_version='v1',
    ),
    patterns=[path('api/core/events/', include('core.api.event.urls'))],
    public=True,
    permission_classes=(IsAdminUser,),
)

router = SimpleRouter()
router.register('', EventViewSet)

urlpatterns = [
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0)),
    path('docs/redoc/', schema_view.with_ui('redoc', cache_timeout=0)),
    *router.urls,
]
