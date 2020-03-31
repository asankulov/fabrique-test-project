from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import RetrieveAPIView, get_object_or_404
from rest_framework.viewsets import ModelViewSet

from applications.models import Application
from applications.serializers import ApplicationSerializer, ApplicationQueryParamSerializer


class ApplicationViewSet(ModelViewSet):
    serializer_class = ApplicationSerializer
    queryset = Application.objects.all()


class TestView(RetrieveAPIView):
    serializer_class = ApplicationSerializer
    queryset = Application.objects.all()

    @swagger_auto_schema(manual_parameters=[openapi.Parameter('access_key',
                                                              openapi.IN_QUERY,
                                                              type=openapi.TYPE_STRING)])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_object(self):
        serializer = ApplicationQueryParamSerializer(data=self.request.query_params)
        serializer.is_valid(raise_exception=True)
        validated_params = serializer.data

        return get_object_or_404(access_key=validated_params.get('access_key'),
                                 queryset=self.get_queryset())
