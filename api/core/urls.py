from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TalkViewSet

router = DefaultRouter()
router.register(r'talks', TalkViewSet)

urlpatterns = [
    path("", include(router.urls))
]
