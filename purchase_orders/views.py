from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED, HTTP_200_OK
from rest_framework.viewsets import ViewSet

from purchase_orders.serializers import PurchaseOrdersCreationSerializer, PurchaseOrdersSerializer, \
    PurchaseOrdersDetailsSerializer, CashbackQuerySerializer, CashbackTotalSerializer
from purchase_orders.services import PurchaseOrdersService


class PurchaseOrdersViewSet(ViewSet):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.purchase_orders_service = PurchaseOrdersService()

    @swagger_auto_schema(request_body=PurchaseOrdersCreationSerializer,
                         responses={201: openapi.Response('response description', PurchaseOrdersSerializer),
                                    400: 'bad request'})
    @action(methods=['POST'], detail=False)
    def create_new_order(self, request):
        serializer = PurchaseOrdersCreationSerializer(data=request.data)

        if serializer.is_valid():
            try:
                purchase_order = self.purchase_orders_service.create_new_order(serializer.data)
                return Response(data=PurchaseOrdersSerializer(purchase_order).data, status=HTTP_201_CREATED)
            except Exception as e:
                return Response(data=str(e), status=HTTP_400_BAD_REQUEST)
        else:
            return Response(data=serializer.errors, status=HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={200: openapi.Response('response description',
                                                          PurchaseOrdersDetailsSerializer(many=True)),
                                    400: 'bad request'})
    @action(methods=['GET'], detail=False)
    def list_orders(self, request):
        try:
            purchase_orders = self.purchase_orders_service.get_all_orders()
            return Response(data=PurchaseOrdersDetailsSerializer(purchase_orders, many=True).data, status=HTTP_200_OK)
        except Exception as e:
            return Response(data=str(e), status=HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(query_serializer=CashbackQuerySerializer,
                         responses={200: openapi.Response('response description',CashbackTotalSerializer),
                                    400: 'bad request'})
    @action(methods=['GET'], detail=False)
    def get_cashback_total(self, request):
        try:
            data = self.purchase_orders_service.get_cashback_total(request.query_params['cpf'])
            return Response(CashbackTotalSerializer(data).data, status=HTTP_200_OK)
        except Exception as e:
            return Response(data=str(e), status=HTTP_400_BAD_REQUEST)

