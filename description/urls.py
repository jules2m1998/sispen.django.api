from django.urls import path
from .views import DescriptionAPIView, DescriptionDetailAPIView

urlpatterns = [
    path('', DescriptionAPIView.as_view()),
    path('<int:id>', DescriptionDetailAPIView.as_view()),
]
