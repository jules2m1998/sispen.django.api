from util.utils import APIView, DetailAPIView
from .models import Description
from .serializers import DescriptionSerializer

queryset = Description.objects.all()


class DescriptionAPIView(APIView):
    queryset = queryset
    serializer_class = DescriptionSerializer


class DescriptionDetailAPIView(DetailAPIView):
    queryset = queryset
    serializer_class = DescriptionSerializer
