from rest_framework import serializers

from purchase_orders.models import PurchaseOrder


class PurchaseOrdersCreationSerializer(serializers.Serializer):
    cpf = serializers.CharField(required=True, max_length=11, min_length=11)
    code = serializers.IntegerField(required=True)
    value = serializers.FloatField(required=True)
    date = serializers.DateTimeField(required=True)


class PurchaseOrdersSerializer(serializers.ModelSerializer):
    cpf = serializers.CharField(source='user.cpf', min_length=11, max_length=11)

    class Meta:
        model = PurchaseOrder
        fields = ['id', 'code', 'value', 'status', 'cpf', 'date']


class PurchaseOrdersDetailsSerializer(serializers.Serializer):
    code = serializers.IntegerField(required=True)
    value = serializers.FloatField(required=True)
    date = serializers.DateTimeField(required=True)
    cashback_value = serializers.FloatField(required=True)
    cashback_percentage = serializers.IntegerField(required=True)
    status = serializers.CharField(required=True)


class CashbackQuerySerializer(serializers.Serializer):
    cpf = serializers.CharField(required=True, max_length=11, min_length=11)


class CashbackTotalSerializer(serializers.Serializer):
    credit = serializers.IntegerField(required=True)
