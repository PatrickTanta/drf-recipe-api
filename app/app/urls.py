from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)

from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # documentation
    path('api/schema/', SpectacularAPIView.as_view(), name='api-schema'),
    path(
        'api/docs/',
        SpectacularSwaggerView.as_view(url_name='api-schema'),
        name='api-docs'
    ),

    # api
    path('api/user/', include('user.urls'), name='user'),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_row = settings.MEDIA_ROOT
    )