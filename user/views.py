from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED
from rest_framework.viewsets import ViewSet

from user.serializers import UserSerializer, UserCreationSerializer
from user.services import UserService


class UsersViewSet(ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user_service = UserService()

    @swagger_auto_schema(request_body=UserCreationSerializer)
    @action(methods=['POST'], url_path='users', detail=False)
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