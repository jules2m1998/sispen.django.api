from django.urls import path
from .views import ContactAPIView, ContactDetailAPIView


urlpatterns = [
    path('', ContactAPIView.as_view(), name='contact'),
    path('<int:id>', ContactDetailAPIView.as_view(), name='contact-detail'),
]