from django.urls import path, include

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from rest_framework.permissions import IsAdminUser
from rest_framework_jwt.views import obtain_jwt_token

from api.auth.views import UserProfileRetrieveView

app_name = 'auth'

schema_view = get_schema_view(
    openapi.Info(
        title="Трансляции. API Авторизации",
        default_version='v1',
    ),
    patterns=[path('api/auth/', include('api.auth.urls'))],
    public=True,
    permission_classes=(IsAdminUser,),
)

urlpatterns = [
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0)),
    path('docs/redoc/', schema_view.with_ui('redoc', cache_timeout=0)),
    path('token/', obtain_jwt_token),
    path('profile/', UserProfileRetrieveView.as_view()),
]
