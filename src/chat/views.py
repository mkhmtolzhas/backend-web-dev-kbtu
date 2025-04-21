from rest_framework import viewsets
from .models import Chat
from message.models import Message
from message.serializers import MessageSerializer
from .serializers import ChatSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class ChatViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Chat instances.
    """
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

    @action(detail=True, methods=['get'])
    def messages(self, request, pk=None):
        """
        Retrieve all messages for a specific chat.
        """
        chat = self.get_object()
        messages = Message.objects.filter(chat=chat)
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)
