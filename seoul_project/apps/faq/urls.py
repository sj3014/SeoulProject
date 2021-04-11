from django.urls import path
from .views import *

urlpatterns = [
    path('', FaqListAPIView.as_view()),
    path('<int:pk>', FaqDetailAPIView.as_view())
]
