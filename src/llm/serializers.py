from rest_framework import serializers

class LLMRequestSerializer(serializers.Serializer):
    prompt = serializers.CharField(max_length=1000, required=True)
