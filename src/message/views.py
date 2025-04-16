from rest_framework import viewsets
from .models import Message
from .serializers import MessageSerializer

class MessageViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Message instances.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer