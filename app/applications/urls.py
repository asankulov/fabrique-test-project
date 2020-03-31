from django.urls import path
from rest_framework.routers import DefaultRouter

from applications.views import ApplicationViewSet,  TestView

router = DefaultRouter()
router.register('application', ApplicationViewSet)

urlpatterns = [
    *router.urls,
    path('test/', TestView.as_view())
]
