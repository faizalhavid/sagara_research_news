
from django.contrib import admin
from django.urls import path, include
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from whitepapers.views import UpcomingWhitePaper, serve_uploaded_file
from rest_framework.routers import DefaultRouter

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

router = DefaultRouter()
router.register('upcoming-whitepaper', UpcomingWhitePaper ,  basename="upcoming-whitepaper")
urlpatterns = router.urls

urlpatterns = [
    
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('whitepapers/', include('whitepapers.urls')),
    path('media/<str:folder>/<str:subfolder>/<str:file_name>/', serve_uploaded_file, name='serve_uploaded_file'),   
    
]
urlpatterns += router.urls