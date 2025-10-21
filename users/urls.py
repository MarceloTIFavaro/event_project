from django.urls import path

from events.urls import urlpatterns
from . import views 

urlpatterns = [
    path("", views.index, name="index")
]