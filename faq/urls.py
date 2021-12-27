from django.urls import path
from .views import FAQAPIView, FAQDetailAPIView


urlpatterns = [
    path('', FAQAPIView.as_view()),
    path('<int:id>', FAQDetailAPIView.as_view()),
]
