from django.urls import path
from .views import *

urlpatterns = [
    #path('', UniversityAdminListAPIView.as_view()),
    #path('<uuid:uuid>', UniversityAdminDetailAPIView.as_view()),
    path('student', university_student_list_view),
    path('student/<str:uuid>', university_student_detail_view),
    path('login', login_view),
    path('signup', signup_view)
]
