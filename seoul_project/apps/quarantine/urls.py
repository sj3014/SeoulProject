from django.urls import path
from .views import *

urlpatterns = [
    path('', QuarantineListAPIView.as_view()),
    path('<uuid:uuid>', QuarantineDetailAPIView.as_view())
]
