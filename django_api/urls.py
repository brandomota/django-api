from django.conf.urls import url
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import routers

from resender_api.views import ResenderViewSet

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description"
   ),
   public=True,
)

router = routers.DefaultRouter()
router.register(r'resender', ResenderViewSet, basename='resender')

urlpatterns = [
    path('', include(router.get_urls())),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
