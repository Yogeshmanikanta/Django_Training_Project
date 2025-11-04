from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),       # ✅ include home route here
    path('faculty/', include('faculty.urls')),
    path('students/', include('students.urls')),
]
