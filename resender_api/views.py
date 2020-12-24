from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.viewsets import ViewSet

class ResenderViewSet(ViewSet):

    @action(methods=['POST'], url_path='users', detail=False)
    def create_user(self, request):
        return Response(data=None, status=HTTP_400_BAD_REQUEST)