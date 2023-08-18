from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .serializers import UsersSerializers

class UserAPIView(GenericAPIView):
    def post(self, request):
        serializer_class = UsersSerializers(data=request.data)
        return Response({'message': 'Got some data!'})
