import json
import requests_mock
from django.test import TestCase
from django.conf import settings
from rest_framework.test import APIClient


class PurchaseOrdersTest(TestCase):

    fixtures = ['fixtures']

    def setUp(self):
        self.test_server = APIClient()
        token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJuYW1lIjoidXNlciAxIiwiZW1haWwiOiJ1c2VyMUB0ZXN0' + \
                     'LmNvbSIsImNyZWF0ZWRfYXQiOiIxMi8yNi8yMDIwLTE1OjU0OjU2In0.LRpRol16fS-Ik-zKH7O3QudB3U0zet0MEhMuyjuZtUo'
        self.headers = {'HTTP_token': token}

    def test_create_purchase_order(self):
        body = {
            "cpf": "70252617002",
            "code": 10,
            "value": 100.00,
            "date": "2020-12-26T00:55:48.100Z"
        }
        response = self.test_server.post('/purchase_orders/create_new_order/', data=json.dumps(body),
                                         content_type='application/json', **self.headers)
        data = response.json()

        self.assertEqual(response.status_code, 201, 'the status code is incorrect')
        self.assertEqual(data['cpf'], '70252617002', 'the cpf returned is incorrect')
        self.assertEqual(data['code'], 10, 'the code returned is incorrect')
        self.assertEqual(data['value'], 100.00, 'the value returned is incorrect')
        self.assertEqual(data['date'], '2020-12-26T00:55:48.100000Z', 'the date returned is incorrect')
        self.assertEqual(data['status'], 'EM_VALIDACAO', 'the status returned is incorrect')

    def test_create_purchase_order_with_invalid_cpf(self):
        body = {
            "cpf": "11111111112",
            "code": 2,
            "value": 100.00,
            "date": "2020-12-26T00:55:48.100Z"
        }
        response = self.test_server.post('/purchase_orders/create_new_order/', data=json.dumps(body),
                                         content_type='application/json', **self.headers)
        data = response.json()
        self.assertEqual(response.status_code, 400, 'the status code is incorrect')
        self.assertEqual(data, 'CPF invalid', 'the response message is incorrect')

    def test_create_purchase_order_with_user_not_found(self):
        body = {
            "cpf": "07783068014",
            "code": 2,
            "value": 100.00,
            "date": "2020-12-26T00:55:48.100Z"
        }
        response = self.test_server.post('/purchase_orders/create_new_order/', data=json.dumps(body),
                                         content_type='application/json', **self.headers)
        data = response.json()
        self.assertEqual(response.status_code, 400, 'the status code is incorrect')
        self.assertEqual(data, 'user not found!', 'the response message is incorrect')

    def test_create_purchase_order_with_user_in_approval_automatic_list(self):
        body = {
            "cpf": "15350946056",
            "code": 20,
            "value": 100.00,
            "date": "2020-12-26T00:55:48.100Z"
        }
        response = self.test_server.post('/purchase_orders/create_new_order/', data=json.dumps(body),
                                         content_type='application/json', **self.headers)
        data = response.json()

        self.assertEqual(response.status_code, 201, 'the status code is incorrect')
        self.assertEqual(data['cpf'], '15350946056', 'the cpf returned is incorrect')
        self.assertEqual(data['code'], 20, 'the code returned is incorrect')
        self.assertEqual(data['value'], 100.00, 'the value returned is incorrect')
        self.assertEqual(data['date'], '2020-12-26T00:55:48.100000Z', 'the date returned is incorrect')
        self.assertEqual(data['status'], 'APROVADO', 'the status returned is incorrect')

    def test_calculate_cashback_orders(self):
        response = self.test_server.get('/purchase_orders/list_orders/',None, **self.headers)

        data = response.json()
        order_1 = next(item for item in data if item["code"] == 1)
        order_2 = next(item for item in data if item["code"] == 2)
        order_3 = next(item for item in data if item["code"] == 3)
        order_4 = next(item for item in data if item["code"] == 4)
        order_5 = next(item for item in data if item["code"] == 5)
        order_6 = next(item for item in data if item["code"] == 6)
        order_7 = next(item for item in data if item["code"] == 7)

        self.assertEqual(response.status_code, 200, 'the status code is incorrect')
        self.assertEqual(order_1['value'], 100.0, 'the value for order is invalid')
        self.assertEqual(order_1['cashback_value'], 10.0, 'the value for chashback is invalid')
        self.assertEqual(order_1['cashback_percentage'], 10, 'the value for cashback percentage is invalid')
        self.assertEqual(order_2['value'], 1000.0, 'the value for order is invalid')
        self.assertEqual(order_2['cashback_value'], 100.0, 'the value for chashback is invalid')
        self.assertEqual(order_2['cashback_percentage'], 10, 'the value for cashback percentage is invalid')
        self.assertEqual(order_3['value'], 500.0, 'the value for order is invalid')
        self.assertEqual(order_3['cashback_value'], 50.0, 'the value for chashback is invalid')
        self.assertEqual(order_3['cashback_percentage'], 10, 'the value for cashback percentage is invalid')
        self.assertEqual(order_4['value'], 1500.0, 'the value for order is invalid')
        self.assertEqual(order_4['cashback_value'], 225.0, 'the value for chashback is invalid')
        self.assertEqual(order_4['cashback_percentage'], 15, 'the value for cashback percentage is invalid')
        self.assertEqual(order_5['value'], 500.0, 'the value for order is invalid')
        self.assertEqual(order_5['cashback_value'], 75.0, 'the value for chashback is invalid')
        self.assertEqual(order_5['cashback_percentage'], 15, 'the value for cashback percentage is invalid')
        self.assertEqual(order_6['value'], 500.0, 'the value for order is invalid')
        self.assertEqual(order_6['cashback_value'], 100.0, 'the value for chashback is invalid')
        self.assertEqual(order_6['cashback_percentage'], 20, 'the value for cashback percentage is invalid')
        self.assertEqual(order_7['value'], 5000.0, 'the value for order is invalid')
        self.assertEqual(order_7['cashback_value'], 1000.0, 'the value for chashback is invalid')
        self.assertEqual(order_7['cashback_percentage'], 20, 'the value for cashback percentage is invalid')

    @requests_mock.Mocker()
    def test_get_cashback_total_for_external_api(self,mock):
        mock.get(settings.CASHBACK_API_HOST+"v1/cashback", text='{"body": {"credit":1000}}')
        response = self.test_server.get('/purchase_orders/get_cashback_total/?cpf=22222222222',
                                        None,**self.headers)

        data = response.json()
        self.assertEqual(response.status_code, 200, 'the status code is incorrect')
        self.assertEqual(data['credit'], 1000, 'the credit returned is incorrect')