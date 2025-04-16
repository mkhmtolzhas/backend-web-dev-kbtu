from rest_framework import viewsets
from .models import Chat
from .serializers import ChatSerializer

class ChatViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Chat instances.
    """
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
