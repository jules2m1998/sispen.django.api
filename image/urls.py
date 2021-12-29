from django.urls import path
from .views import ImageAPIView, ImageDetailAPIView

urlpatterns = [
    path('', ImageAPIView.as_view(), name='image-api'),
    path('<int:id>', ImageDetailAPIView.as_view(), name='image-api'),
]