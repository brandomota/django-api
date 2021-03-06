![Main Build](https://circleci.com/gh/brandomota/django-api/tree/main.svg?style=svg)
# django-api
API Django para desafio técnico

## Requisitos para execução
- banco de dados PostgreSQL
- Python 3.8+

## Variáveis de ambiente do sistema
- `SECRET_KEY` : chave secreta da API utilizada para a criptografia das senhas. **defina uma nova ao executar em produção essa API**;
- `DEBUG_MODE`: ativa o modo de depuração da API, ativado por padrão. Recomenda-se desativar ao rodar em um ambiente de produção;
- `API_HOSTNAME`: hostname dns/ endereço IP do servidor da API;
- `DATABASE_NAME`: nome do banco de dados da API;
- `DATABASE_HOST`: endereço do servidor do banco de dados da API;
- `DATABASE_PORT`: porta de acesso do banco de dados da API;
- `DATABASE_USERNAME`: usuário do banco de dados da API;
- `DATABASE_PASSWORD`: senha de acesso do banco de dados da API;
- `CASHBACK_API_HOST`: endereço da API cashback;
- `CASHBACK_API_TOKEN`: token de acesso API cashback.

## Instruções para execução local

- execute a instalação dos pacotes utilizados no sistema: `pip install -r requirements.txt`;
- defina as variáveis de ambiente ou altere manualmente em `django_api/settings.py`;
- execute as migrations do projeto: `python manage.py migrate`;
- inicie o devserver da API: `python manage.py runserver`.
- para executar os testes da API,execute: `python manage.py test`

## Informações adicionais
- imagem docker podendo ser encontrada no endereço [`https://hub.docker.com/r/brandomota/django-api`](https://hub.docker.com/r/brandomota/django-api)
- URL de acesso do projeto publicado no Heroku em [`https://brando-django-api.herokuapp.com/`](https://brando-django-api.herokuapp.com/)
- documentação da api acessível na rota `/swagger`