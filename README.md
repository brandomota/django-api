# django-api
API Django para desafio técnico

## Requisitos para execução
- banco de dados PostgreSQL
- Python 3.8+

##Variáveis de ambiente do sistema
- `API_SECRET_KEY` : chave secreta da API utilizada para a criptografia das senhas. **defina uma nova ao executar em produção essa API**;
- `DEBUG_MODE`: ativa o modo de depuração da API, ativado por padrão. Recomenda-se desativar ao rodar em um ambiente de produção;
- `API_HOSTNAME`: hostname dns/ endereço IP do servidor da API;
- `DATABASE_NAME`: nome do banco de dados da API;
- `DATABASE_HOST`: endereço do servidor do banco de dados da API;
- `DATABASE_PORT`: porta de acesso do banco de dados da API;
- `DATABASE_USERNAME`: usuário do banco de dados da API;
- `DATABASE_PASSWORD`: senha de acesso do banco de dados da API;
- `CASHBACK_API_HOST`: endereço da API cashback;
- `CASHBACK_API_TOKEN`: token de acesso API cashback.

##Instruções para execução local

- execute a instalação dos pacotes utilizados no sistema: `pip install -r requirements.txt`;
- defina as variáveis de ambiente ou altere manualmente em `django_api/settings.py`;
- execute as migrations do projeto: `python manage.py migrate`;
- inicie o devserver da API: `python manage.py runserver`.
