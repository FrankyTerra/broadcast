from django.urls import path, include

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from rest_framework.permissions import IsAdminUser

app_name = 'api'

schema_view = get_schema_view(
    openapi.Info(
        title="Broadcast API",
        default_version='v1',
    ),
    patterns=[path('api/', include('api.urls'))],
    public=True,
    permission_classes=(IsAdminUser,),
)

urlpatterns = [
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0)),
    path('docs/redoc/', schema_view.with_ui('redoc', cache_timeout=0)),
    path('auth/', include('api.auth.urls')),
    path('core/', include('core.api.urls')),
    path('users/', include('user.api.urls')),
]
