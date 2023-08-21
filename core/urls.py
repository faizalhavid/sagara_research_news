
from django.contrib import admin
from django.urls import path, include
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from whitepapers.views import WhitePapersList, UpcomingWhitePaper, serve_uploaded_file
from users.views import UserDownload
from rest_framework.routers import DefaultRouter
from users.views import UserDownload

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [

    path('', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('whitepapers/',
         WhitePapersList.as_view({'get': 'list'}), name='whitepapers-list'),
    path('whitepapers/<str:slug>/',
         WhitePapersList.as_view({'get': 'retrieve'}), name='whitepapers-detail'),
    path('media/<str:folder>/<str:subfolder>/<str:file_name>/',
         serve_uploaded_file, name='serve_uploaded_file'),
    path('upcoming-whitepaper/', UpcomingWhitePaper.as_view({'get': 'list'})),
    path('user-download/<int:whitepapers_id>/', UserDownload.as_view({'post': 'user_download'}), name='user-download'),
  


]
# router = DefaultRouter()
# router.register(r'upcoming-whitepaper', UpcomingWhitePaper ,  basename="upcoming-whitepaper")
# urlpatterns = router.urls
# urlpatterns += router.urls
