from django.urls import path
from .views import *

urlpatterns = [
    path('', AdminUserListAPIView.as_view()),
    path('<uuid:uuid>', AdminUserDetailAPIView.as_view())
]
