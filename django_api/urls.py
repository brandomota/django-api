from django.conf.urls import url
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import routers

from purchase_orders.views import PurchaseOrdersViewSet
from user.views import UsersViewSet

schema_view = get_schema_view(
   openapi.Info(
      title="Django API",
      default_version='v1',
      description="API Django"
   ),
   public=True,
)

router = routers.DefaultRouter()
router.register('users', UsersViewSet, basename='users')
router.register('purchase_orders', PurchaseOrdersViewSet, basename='purchase_orders')

urlpatterns = [
    path('', include(router.get_urls())),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
