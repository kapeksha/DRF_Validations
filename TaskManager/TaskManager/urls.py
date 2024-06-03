

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # URL pattern for accessing Django admin site
    path('api/', include('mytaskmanager.urls')),  # URL pattern for including API endpoints from mytaskmanager app
]
