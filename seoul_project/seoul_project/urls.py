from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('apps.student.urls')),
    path('api/adminUser/', include('apps.universityAdmin.urls')),
    path('api/address/', include('apps.address.urls')),
    path('api/country/', include('apps.country.urls')),
    path('api/university/', include('apps.university.urls')),
    path('api/quarantine/', include('apps.quarantine.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
