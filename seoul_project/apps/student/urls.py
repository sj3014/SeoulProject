from django.urls import path
from .views import *

urlpatterns = [
    path('', StudentListAPIView.as_view()),
    path('<uuid:uuid>', StudentDetailAPIView.as_view()),
    path('login', login_view),
    path('signup', signup_view)
]
