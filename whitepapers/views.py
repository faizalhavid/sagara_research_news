from rest_framework import viewsets
from .serializers import WhitePaperListSerializers, WhitePaperDetailSerializers
from .models import WhitePapers, Topic, WhitePapersDownload
from django.shortcuts import get_object_or_404 , reverse
from django.http import FileResponse
from django.conf import settings
from django.utils import timezone
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from django.http import Http404, HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import F
import os
class WhitePapersList(viewsets.ViewSet):
    serializer_class = WhitePaperListSerializers
    
    def list(self, request):
        queryset = WhitePapers.objects.all()
        serializer = WhitePaperListSerializers(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, slug=None):
        item = str(self.kwargs.get('slug').lower())
        whitepaper = get_object_or_404(WhitePapers, slug__iexact=item)
        serializer = WhitePaperDetailSerializers(whitepaper)
        whitepaper_id = whitepaper.id
        return Response(serializer.data)
        # return HttpResponseRedirect(reverse('user-download', args=[whitepaper_id]))
    
    # def get_object(self, queryset=None, **kwargs):
    #     item = str(self.kwargs.get('pk').lower())
    #     return get_object_or_404(WhitePapers, slug__iexact=item)

    # def get_queryset(self):
    #     return WhitePapers.objects.all()
    

class UpcomingWhitePaper(viewsets.ViewSet):
    def list(self, request):
        queryset = WhitePapers.objects.filter(published_at__lte=timezone.now()).order_by('-published_at')[:2]
        serializer = WhitePaperListSerializers(queryset, many=True)
        return Response(serializer.data)
    
    # def retrieve(self, request, slug=None):
    #     permission_classes = IsAuthenticated
    #     item = str(self.kwargs.get('slug'))
    #     upwhitepapers = get_object_or_404(WhitePapers, slug__iexact=item)
    #     serializer = WhitePaperDetailSerializers(upwhitepapers)
    #     return Response(serializer.data)

def is_pdf_file(file_name):
    _, file_extension = os.path.splitext(file_name)
    return file_extension.lower() == '.pdf'

@api_view(['GET'])
@swagger_auto_schema(
    operation_summary="Serve Uploaded File",
    operation_description="Serve an uploaded file from the media folder.",
    responses={200: 'File content'}
)
def serve_uploaded_file(request, folder, subfolder, file_name , user_id = None):
    file_path = os.path.join(settings.MEDIA_ROOT, folder, subfolder, file_name)
    try:
        user_id = request.GET.get('user_id')
        if user_id is not None:
            if os.path.exists(file_path) and os.path.isfile(file_path) and is_pdf_file(file_name):
                    whitepaper = WhitePapers.objects.filter(pdf__icontains=file_name).first()
                    WhitePapers.objects.filter(pdf__icontains=file_name).update(count_of_downloads=F('count_of_downloads') + 1)
                    WhitePapersDownload.objects.create(user_id=user_id, whitepaper_id=whitepaper.id)
        return FileResponse(open(file_path, 'rb'), as_attachment=True)

    except Exception as e:    
        return Response({'message': 'File not found.' + str(e)}, status=404)