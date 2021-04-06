from django.urls import path
from .views import *

urlpatterns = [
    path('', UniversityListAPIView.as_view()),
    path('<int:pk>', UniversityDetailAPIView.as_view())
]
