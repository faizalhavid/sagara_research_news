from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UsersSerializers
from whitepapers.models import WhitePapers
from whitepapers.serializers import WhitePaperDetailSerializers
from django.http import  HttpResponseRedirect
from django.shortcuts import reverse
from whitepapers.views import serve_uploaded_file
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import ValidationError


class UserDownload(APIView):
    serializer_class = UsersSerializers
    permission_classes = [AllowAny]
    def post(self, request , slug):
        serializer = UsersSerializers(data=request.data, required=True)
        user_id = None
        try :
            if serializer.is_valid():
                new_user = serializer.save()
                user_id = new_user.id
            else: 
                error_list = []
                for field, errors in serializer.errors.items():
                    for error in errors:
                        error_list.append({'field': field, 'message': error})
                return Response({'message': error_list}, status=400)
            whitepapers = WhitePapers.objects.get(slug=slug)
            media_path = str(whitepapers.pdf)
            folder, subfolder, file_name = media_path.split('/')       
            url = reverse('serve_uploaded_file', kwargs={'folder': folder, 'subfolder': subfolder, 'file_name': file_name})
            url += f'?user_id={user_id}'
            return HttpResponseRedirect(url)
        except Exception as e:
            return Response({'message': str(e)} , status=404)
