from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import LLMRequestSerializer
from .usecases import llm_use_case

class LLMView(APIView):
    def post(self, request):
        serializer = LLMRequestSerializer(data=request.data)
        if serializer.is_valid():
            prompt = serializer.validated_data['prompt']

            response_text = llm_use_case.generate_response(prompt)

            return Response({"response": response_text}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
