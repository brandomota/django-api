import json

from django.test import TestCase
from rest_framework.test import APIClient

class UserTest(TestCase):
    fixtures = ['fixtures']
    def setUp(self):
        self.test_server = APIClient()

    def test_login_with_cpf_of_existing_user(self):
        body = {
            "login": "70252617002",
            "password": "test"
        }
        response = self.test_server.post('/users/login/', data=json.dumps(body),
                                         content_type='application/json')
        self.assertEqual(response.status_code, 200, 'the status code are incorrect')
        self.assertIsNotNone(response.data, 'the token body returned is empty')

    def test_login_with_email_of_existing_user(self):
        body = {
            "login": "user1@test.com",
            "password": "test"
        }
        response = self.test_server.post('/users/login/', data=json.dumps(body),
                                         content_type='application/json')
        self.assertEqual(response.status_code, 200, 'the status code are incorrect')
        self.assertIsNotNone(response.data, 'the token body returned is empty')

    def test_login_with_incorrect_email(self):
        body = {
            "login": "user_incorrect@test.com",
            "password": "test"
        }
        response = self.test_server.post('/users/login/', data=json.dumps(body),
                                         content_type='application/json')
        self.assertEqual(response.status_code, 401, 'the status code is incorrect')
        self.assertEqual(response.data, 'User not found', 'the body response is incorrect')

    def test_login_with_incorrect_cpf(self):
        body = {
            "login": "12312312312",
            "password": "test"
        }
        response = self.test_server.post('/users/login/', data=json.dumps(body),
                                         content_type='application/json')
        self.assertEqual(response.status_code, 401, 'the status code is incorrect')
        self.assertEqual(response.data, 'User not found', 'the body response is incorrect')

    def test_login_with_incorrect_password(self):
        body = {
            "login": "user1@test.com",
            "password": "incorrect_password"
        }
        response = self.test_server.post('/users/login/', data=json.dumps(body),
                                         content_type='application/json')
        self.assertEqual(response.status_code, 401, 'the status code is incorrect')
        self.assertEqual(response.data, 'Login incorrect', 'the body response is incorrect')

    def test_create_new_user(self):
        body = {
            "name": "user2",
            "email": "user2@test.com",
            "cpf": "07783068014",
            "password": "test"
        }
        response = self.test_server.post('/users/create_user/', data=json.dumps(body),
                                         content_type='application/json')
        data = response.json()
        self.assertEqual(response.status_code, 201, 'the status code is incorrect')
        self.assertEqual(data['id'], 2, 'new user id is incorrect')
        self.assertEqual(data['name'], 'user2', 'name returned is incorrect')
        self.assertEqual(data['email'], 'user2@test.com', 'email returned is incorrect')
        self.assertEqual(data['cpf'], '07783068014', 'cpf returned is incorrect')
        self.assertEqual('password' in data, False, 'password should be ignored in return object')

    def test_create_new_user_with_invalid_cpf(self):
        body = {
            "name": "user2",
            "email": "user2@test.com",
            "cpf": "11121121112",
            "password": "test"
        }
        response = self.test_server.post('/users/create_user/', data=json.dumps(body),
                                         content_type='application/json')
        data = response.json()
        self.assertEqual(response.status_code, 400, 'the status code is incorrect')
        self.assertEqual(data, 'CPF invalid', 'the message returned is incorrect')

    def test_create_new_user_with_existing_cpf(self):
        body = {
            "name": "user2",
            "email": "user2@test.com",
            "cpf": "70252617002",
            "password": "test"
        }
        response = self.test_server.post('/users/create_user/', data=json.dumps(body),
                                         content_type='application/json')
        data = response.json()
        self.assertEqual(response.status_code, 400, 'the status code is incorrect')
        self.assertEqual(data, 'CPF exists')

    def test_create_new_user_with_existing_email(self):
        body = {
            "name": "user2",
            "email": "user1@test.com",
            "cpf": "07783068014",
            "password": "test"
        }

        response = self.test_server.post('/users/create_user/', data=json.dumps(body),
                                         content_type='application/json')
        data = response.json()
        self.assertEqual(response.status_code, 400, 'the status code is incorrect')
        self.assertEqual(data, 'Email exists')