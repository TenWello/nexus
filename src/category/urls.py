from django.urls import path
from .views import region

urlpatterns = [
    path('', region, name='region')
]