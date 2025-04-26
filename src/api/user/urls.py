from django.urls import path
from .views import ProfileGenericAPIView

urlpatterns = [
    path('', ProfileGenericAPIView.as_view()),
]