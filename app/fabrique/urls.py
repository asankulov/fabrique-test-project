from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Fabrique Test Project",
        default_version='v1',
        description="REST API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="kylych.asankulov@yandex.ru"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,)
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('applications.urls')),
    path('api/docs/', schema_view.with_ui('swagger', cache_timeout=0)),
]
