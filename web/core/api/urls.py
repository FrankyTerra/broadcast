from django.urls import path, include

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from rest_framework.permissions import IsAdminUser


app_name = 'core'

schema_view = get_schema_view(
    openapi.Info(
        title="Core API",
        default_version='v1',
    ),
    patterns=[path('api/core/', include('core.api.urls'))],
    public=True,
    permission_classes=(IsAdminUser,),
)

urlpatterns = [
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0)),
    path('docs/redoc/', schema_view.with_ui('redoc', cache_timeout=0)),
    path('event_types/', include('core.api.event_type.urls')),
    path('events/', include('core.api.event.urls')),
    path('broadcasts/', include('core.api.broadcast.urls')),
    path('comments/', include('core.api.comment.urls')),
]
