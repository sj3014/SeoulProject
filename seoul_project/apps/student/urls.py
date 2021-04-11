from django.urls import path
from .views import *
from apps.quarantine.views import StudentQuarantineAPIView

urlpatterns = [
    #path('', StudentListAPIView.as_view()),
    path('info', StudentInfoAPIView.as_view()),
    path('covid', StudentQuarantineAPIView.as_view()),
    #path('<uuid:uuid>', StudentDetailAPIView.as_view()),
    path('login', login_view),
    path('signup', signup_view)
]
