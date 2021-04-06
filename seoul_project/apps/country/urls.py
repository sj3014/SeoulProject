from django.urls import path
from .views import *

urlpatterns = [
    path('', CountryListAPIView.as_view()),
    path('<int:pk>', CountryDetailAPIView.as_view())
]
