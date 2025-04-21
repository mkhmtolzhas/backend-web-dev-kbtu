from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from .models import File
from .serializers import FileSerializer
from .utils import upload_file_to_s3

class FileViewSet(ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    parser_classes = [MultiPartParser]

    def create(self, request, *args, **kwargs):
        file_obj = request.FILES['file']
        filename = file_obj.name
        content_type = file_obj.content_type

        file_url = upload_file_to_s3(file_obj, filename, content_type)

        file_instance = File.objects.create(
            name=filename,
            content_type=content_type,
            url=file_url
        )

        serializer = self.get_serializer(file_instance)
        return Response(serializer.data)
