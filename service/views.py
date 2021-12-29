from util.utils import APIView, DetailAPIView
from .models import Service
from .serializers import ServiceSerializer

queryset = Service.objects.all()


class ServiceAPIView(APIView):
    queryset = queryset
    serializer_class = ServiceSerializer


class ServiceDetailAPIView(DetailAPIView):
    queryset = queryset
    serializer_class = ServiceSerializer
