from django.urls import path
from .views import main, contact

urlpatterns = [
    path('', main, name='main'),
    path('contact/', contact, name='contact')
]