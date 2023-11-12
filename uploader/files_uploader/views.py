from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import FileSerializer


class FileUploadView(APIView):
    def post(self, request, format=None):
        file_serializer = FileSerializer
        if file_serializer.is_valid():
            file_serializer.save()
            # Celery
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)