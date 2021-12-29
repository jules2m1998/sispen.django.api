from .serializers import CotationTypeSerializer
from .models import CotationType
from util.utils import APIView, DetailAPIView

queryset = CotationType.objects.all()


class CotationTypeAPIView(APIView):
    queryset = queryset
    serializer_class = CotationTypeSerializer


class CotationDetailTypeAPIView(DetailAPIView):
    queryset = queryset
    serializer_class = CotationTypeSerializer
