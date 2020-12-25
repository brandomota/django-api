from validate_docbr import CPF


class Utils:
    def __init__(self):
        self.cpf_validator = CPF()

    def validate_cpf(self, cpf):
        if self.cpf_validator.validate(cpf) is False:
            raise Exception('CPF invalid')
