from django.urls import path, include
from .views import BlogCBView
urlpatterns = [
    path('', BlogCBView.as_view()),
]