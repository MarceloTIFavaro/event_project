from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('events/', include('events.urls')),
    path('users/', include('users.urls')),
    path('admin/', admin.site.urls),
]
