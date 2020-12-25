from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED, HTTP_200_OK, HTTP_401_UNAUTHORIZED
from rest_framework.viewsets import ViewSet

from user.serializers import UserSerializer, UserCreationSerializer, LoginSerializer, TokenSerializer
from user.services import UserService


class UsersViewSet(ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user_service = UserService()

    @swagger_auto_schema(request_body=UserCreationSerializer,
                         responses={201:  openapi.Response('response description', UserSerializer), 400: 'bad request'})
    @action(methods=['POST'], detail=False)
    def create_user(self, request):
        serializer = UserCreationSerializer(data=request.data)
        if serializer.is_valid():
            try:
                result = self.user_service.create_user(serializer.data)

                return Response(data=UserSerializer(result).data, status=HTTP_201_CREATED)
            except Exception as e:
                return Response(data=str(e), status=HTTP_400_BAD_REQUEST)
        else:
            return Response(data=serializer.errors, status=HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=LoginSerializer,
                         responses={401: 'unauthorized',
                                    200: openapi.Response('response description', TokenSerializer)})
    @action(methods=['POST'], url_path='login', detail=False)
    def login(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            try:
                token = self.user_service.login(serializer.data)
                return Response(data=token, status=HTTP_200_OK)
            except Exception as e:
                return Response(data=str(e), status=HTTP_401_UNAUTHORIZED)
        else:
            return Response(data=serializer.errors, status=HTTP_400_BAD_REQUEST)