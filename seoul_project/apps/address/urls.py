from django.urls import path
from .views import *

urlpatterns = [
    path('', AddressListAPIView.as_view()),
    path('<int:pk>', AddressDetailAPIView.as_view())
]
