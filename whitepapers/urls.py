from django.urls import path, include
from .views import WhitePapersList , UpcomingWhitePaper
from rest_framework.routers import DefaultRouter
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

router = DefaultRouter()
router.register('', WhitePapersList, basename='whitepaper')
urlpatterns = router.urls
urlpatterns +=staticfiles_urlpatterns()
urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)