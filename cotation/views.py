from util.utils import APIView, DetailAPIView
from .models import Cotation
from .serializers import CotationSerializer

queryset = Cotation.objects.all()


class CotationAPIView(APIView):
    queryset = queryset
    serializer_class = CotationSerializer


class CotationDetailAPIView(DetailAPIView):
    queryset = queryset
    serializer_class = CotationSerializer
