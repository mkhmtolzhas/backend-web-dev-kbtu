from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import LLMRequestSerializer
from .usecases import llm_use_case
from chat.models import Chat
from message.models import Message
from django.contrib.auth.models import User

class LLMView(APIView):
    def post(self, request):
        serializer = LLMRequestSerializer(data=request.data)
        if serializer.is_valid():
            prompt = serializer.validated_data['prompt']
            file_url = serializer.validated_data.get('file_url')
            chat_id = serializer.validated_data.get('chat_id')

            user = request.user

            try:
                chat = Chat.objects.get(id=chat_id)
            except Chat.DoesNotExist:
                return Response({"error": "Chat not found."}, status=status.HTTP_404_NOT_FOUND)

            user_message = Message.objects.create(
                content=prompt,
                author_type=Message.AuthorType.USER,
                user=user,
                chat=chat
            )

            # Генерация ответа от LLM
            if file_url:
                response_text = llm_use_case.generate_response_from_file(prompt, file_url)
            else:
                response_text = llm_use_case.generate_response(prompt)

            # Сохраняем ответ от LLM
            llm_message = Message.objects.create(
                content=response_text,
                author_type=Message.AuthorType.LLM,
                user=None,
                chat=chat
            )

            return Response({"response": response_text}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
