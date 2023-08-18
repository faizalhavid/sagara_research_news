
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import WhitePaperSerializers
from .models import WhitePapers, Topic
from django.shortcuts import get_object_or_404
from django.shortcuts import render
import os
from django.http import FileResponse
from django.conf import settings
from django.utils import timezone
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from django.http import Http404
class WhitePapersList(viewsets.ModelViewSet):
    serializer_class = WhitePaperSerializers
    
    def get_object(self, queryset=None, **kwargs):
        item = str(self.kwargs.get('pk').lower())
        return get_object_or_404(WhitePapers, slug__iexact=item)

    def get_queryset(self):
        return WhitePapers.objects.all()
class UpcomingWhitePaper(viewsets.ModelViewSet):
    serializer_class = WhitePaperSerializers
    
    def get_object(self, queryset=None, **kwargs):
            item = str(self.kwargs.get('pk').lower())
            return get_object_or_404(WhitePapers, slug__iexact=item)

    def get_queryset(self):
        return WhitePapers.objects.filter(published_at__lte=timezone.now()).order_by('-published_at')[:2]
    
@api_view(['GET'])
@swagger_auto_schema(
    operation_summary="Serve Uploaded File",
    operation_description="Serve an uploaded file from the media folder.",
    responses={200: 'File content'}
)
def serve_uploaded_file(request, folder, subfolder, file_name):
    file_path = os.path.join(settings.MEDIA_ROOT, folder, subfolder, file_name)
    if os.path.exists(file_path) and os.path.isfile(file_path):
        return FileResponse(open(file_path, 'rb'), as_attachment=True)

    raise Http404("File not found")
