"""External API urls."""

from django.urls import include, path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from modoboa.core.extensions import exts_pool

app_name = "api"

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
    path('', include("modoboa.core.api.v2.urls")),
    path('', include("modoboa.admin.urls_api")),
    path('', include("modoboa.parameters.api.v2.urls")),
    path('', include("modoboa.limits.urls_api")),
    path('', include("modoboa.relaydomains.urls_api")),
    path('', include("modoboa.dnstools.api.v2.urls")),
]

urlpatterns += exts_pool.get_urls(category="api")