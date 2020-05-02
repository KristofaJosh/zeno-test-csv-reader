from django.urls import path, include
from rest_framework import routers
from .views import ZenoCsvViewSet, ZenoFileUploadView

router = routers.DefaultRouter()
router.register('csv_db', ZenoCsvViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('upload/', ZenoFileUploadView.as_view())
]
