from util.utils import APIView, DetailAPIView
from .models import Contact
from .serializers import ContactSerializer

queryset = Contact.objects.all()


class ContactAPIView(APIView):
    queryset = queryset
    serializer_class = ContactSerializer


class ContactDetailAPIView(DetailAPIView):
    queryset = queryset
    serializer_class = ContactSerializer
