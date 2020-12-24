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

    def __validate_cpf(self, cpf):
        if self.cpf_validator.validate(cpf) is False:
            raise Exception('CPF invalid')

    def __generate_password_hash(self, password):
        return pbkdf2_sha256.hash(password)
