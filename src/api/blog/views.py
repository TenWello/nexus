from django.http import HttpResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import BlogSerializer
from blog.models import Blog


class BlogCBView(APIView):
    def get(self, request):
        categories = Blog.objects.all()
        result = BlogSerializer(categories, many=True)
        return Response({'data': result.data}, status=status.HTTP_200_OK)


    def post(self, request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
