import jwt
from django.conf import settings
from rest_framework import authentication, exceptions

from user.models import User


class ApiAuth(authentication.BaseAuthentication):
    def authenticate(self, request):
        try:
            if 'token' not in request.headers:
                raise Exception('No token found')

            token = request.headers['token']

            token_payload = jwt.decode(token,key=settings.SECRET_KEY, algorithms='HS256')

            user = User.objects.get(email=token_payload['email'])
            return user, None
        except Exception as e:
            raise exceptions.AuthenticationFailed(str(e))