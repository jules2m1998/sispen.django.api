from django.urls import path
from .views import CotationAPIView, CotationDetailAPIView


urlpatterns = [
    path('', CotationAPIView.as_view()),
    path('<int:id>', CotationDetailAPIView.as_view()),
]