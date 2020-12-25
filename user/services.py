import jwt, hashlib
from datetime import datetime
from django.db.models import Q
from django.conf import settings
from passlib.hash import pbkdf2_sha256
from validate_docbr import CPF
from user.models import User


class UserService:

    def __init__(self):
        self.cpf_validator = CPF()

    def create_user(self, data):
        self.__validate_cpf(data['cpf'])
        try:
            new_user = User(cpf=data['cpf'],
                            name=data['name'],
                            email=data['email'],
                            password=self.__generate_password_hash(data['password']))
            new_user.save()
            return new_user
        except Exception as e:
            raise e

    def login(self, data):
        try:
            user = User.objects.filter(Q(cpf=data['login']) | Q(email=data['login'])).first()
            if user.password == str(self.__generate_password_hash(data['password'])):
                payload_data = {
                    'name': user.name,
                    'email': user.email,
                    'created_at': datetime.strftime(datetime.now(), '%m/%d/%Y-%H:%M:%S')
                }

                token = jwt.encode(payload_data, settings.SECRET_KEY, algorithm='HS256')
                return token
            else:
                raise Exception('Login incorrect')
        except Exception as e:
            raise e

    def __validate_cpf(self, cpf):
        if self.cpf_validator.validate(cpf) is False:
            raise Exception('CPF invalid')

    def __generate_password_hash(self, password):
        crypto_module = hashlib.sha256()
        crypto_module.update((password + settings.SECRET_KEY).encode('UTF-8'))
        return crypto_module.digest()
