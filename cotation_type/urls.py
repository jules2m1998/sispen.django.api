from django.urls import path
from .views import CotationTypeAPIView, CotationDetailTypeAPIView

urlpatterns = [
    path('', CotationTypeAPIView.as_view()),
    path('<int:id>', CotationDetailTypeAPIView.as_view()),
]