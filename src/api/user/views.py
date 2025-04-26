from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from user.models import Profile
from .serializers import UserSerializer

class ProfileGenericAPIView(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Profile.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request)
    def post(self, request, *args, **kwargs):
        return self.create(request)