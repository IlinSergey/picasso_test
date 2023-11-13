from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser, MultiPartParser
from rest_framework import generics

from .models import File
from .serializers import FileSerializer
from .tasks import start_process_file


class FileUploadView(APIView):
    parser_classes = [FileUploadParser,]

    def post(self, request, format=None):
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_object = file_serializer.save()
            start_process_file.delay(file_id=file_object.id)
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FileListView(generics.ListAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
