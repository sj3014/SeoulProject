from django.urls import path
from .views import *

urlpatterns = [
    path('', UniversityAdminListAPIView.as_view()),
    path('<uuid:uuid>', UniversityAdminDetailAPIView.as_view())
]
