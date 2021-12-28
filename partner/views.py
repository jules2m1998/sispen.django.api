from util.utils import APIView, DetailAPIView
from .models import Partner
from .serializers import PartnerSerializer


class PartnerAPIView(APIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer


class PartnerDetailAPIView(DetailAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
