from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/student/', include('apps.student.urls')),
    path('api/universityAdmin/', include('apps.universityAdmin.urls')),
    path('api/faq/', include('apps.faq.urls')),
    path('api/announcement/', include('apps.announcement.urls')),
    path('api/address/', include('apps.address.urls')),
    path('api/country/', include('apps.country.urls')),
    path('api/university/', include('apps.university.urls')),
    path('api/quarantine/', include('apps.quarantine.urls')),
]
