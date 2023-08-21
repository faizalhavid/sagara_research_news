from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import UsersSerializers
from whitepapers.models import WhitePapers
from whitepapers.serializers import WhitePaperDetailSerializers
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import reverse
from whitepapers.views import serve_uploaded_file

class UserDownload(viewsets.ModelViewSet):
    serializer_class = UsersSerializers
    
    def user_download(self, request , whitepapers_id):
        serializer = UsersSerializers(data=request.data)
        user_id = None
        try :
            if serializer.is_valid():
                new_user = serializer.save()
                user_id = new_user.id
            whitepapers = WhitePapers.objects.get(id=whitepapers_id)
            media_path = str(whitepapers.pdf)
            folder, subfolder, file_name = media_path.split('/')       
            url = reverse('serve_uploaded_file', kwargs={'folder': folder, 'subfolder': subfolder, 'file_name': file_name})
            url += f'?user_id={user_id}'
            return HttpResponseRedirect(url)
        except Exception as e:
            return Response({'error': str(e)})
