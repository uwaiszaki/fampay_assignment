from django.urls import path
from .api import views

urlpatterns = [
        path('', views.SearchVideo.as_view(), name='search'),
]
