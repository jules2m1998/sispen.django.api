from django.urls import path
from .views import PartnerDetailAPIView, PartnerAPIView

urlpatterns = [
    path('', PartnerAPIView.as_view()),
    path('<int:id>', PartnerDetailAPIView.as_view()),
]