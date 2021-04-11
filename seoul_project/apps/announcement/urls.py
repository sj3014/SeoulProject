from django.urls import path
from .views import *

urlpatterns = [
    path('', AnnouncementListAPIView.as_view()),
    path('<int:pk>', AnnouncementDetailAPIView.as_view())
]
