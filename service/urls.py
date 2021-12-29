from django.urls import path
from .views import ServiceAPIView, ServiceDetailAPIView

urlpatterns = [
    path('', ServiceAPIView.as_view()),
    path('<int:id>', ServiceDetailAPIView.as_view()),
 ]
