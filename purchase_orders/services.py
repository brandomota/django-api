from datetime import datetime

from dateutil.relativedelta import relativedelta
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q

from django_api.utils import Utils
from purchase_orders.models import PurchaseOrder
from user.models import User


class PurchaseOrdersService:
    def __init__(self):
        self.allowed_cpf = [
            '15350946056'
        ]
        self.utils = Utils()

    def create_new_order(self, data):
        try:
            self.utils.validate_cpf(data['cpf'])
            user = User.objects.get(cpf=data['cpf'])
            purchase_order = PurchaseOrder(user=user, value=data['value'], code=data['code'], date=data['date'])

            if data['cpf'] in self.allowed_cpf:
                purchase_order.status = PurchaseOrder.PurchaseStatus.APROVADO
            else:
                purchase_order.status = PurchaseOrder.PurchaseStatus.EM_VALIDACAO

            purchase_order.save()
            return purchase_order
        except ObjectDoesNotExist:
            raise Exception('user not found!')
        except Exception as e:
            raise e

    def get_all_orders(self):
        all_orders = PurchaseOrder.objects.all()
        result = []

        for order in all_orders:
            cashback_data = self.__calculate_cashback_order(order)
            data = {
                'code': order.code,
                'value': order.value,
                'status': order.status,
                'date': order.date,
                'cashback_percentage': cashback_data[0],
                'cashback_value': cashback_data[1]

            }
            result.append(data)

        return result

    def __calculate_cashback_order(self, order):
        order_by_user = PurchaseOrder.objects.filter(Q(user=order.user) &
                                                     Q(date__gte=datetime.today() + relativedelta(months=-1)) &
                                                     Q(status=PurchaseOrder.PurchaseStatus.APROVADO))
        total_value = 0

        for o in order_by_user:
            total_value += o.value

        if total_value <= 1000:
            cashback_percentage = 10
        elif 1000 < total_value <= 1500:
            cashback_percentage = 15
        else:
            cashback_percentage = 20

        order_cashback = round((order.value / 100) * cashback_percentage, ndigits=2)

        return cashback_percentage, order_cashback
