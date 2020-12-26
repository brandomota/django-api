import json

from django.test import TestCase
from rest_framework.test import APIClient


class PurchaseOrdersTest(TestCase):

    fixtures = ['fixtures']

    def setUp(self):
        self.test_server = APIClient()

    def test_create_purchase_order(self):
        body = {
            "cpf": "70252617002",
            "code": 2,
            "value": 100.00,
            "date": "2020-12-26T00:55:48.100Z"
        }
        response = self.test_server.post('/purchase_orders/create_new_order/', data=json.dumps(body),
                                         content_type='application/json')
        data = response.json()

        self.assertEqual(response.status_code, 201, 'the status code is incorrect')
        self.assertEqual(data['id'], 2, 'the id returned is incorrect')
        self.assertEqual(data['code'], 2, 'the code returned is incorrect')
        self.assertEqual(data['value'], 100.00, 'the value returned is incorrect')
        self.assertEqual(data['date'], '2020-12-26T00:55:48.100000Z', 'the date returned is incorrect')
        self.assertEqual(data['status'], 'EM_VALIDACAO', 'the status returned is incorrect')
