from rest_framework import serializers
import urllib.parse
import re

class LLMRequestSerializer(serializers.Serializer):
    prompt = serializers.CharField(max_length=1000, required=True)
    file_url = serializers.CharField(required=False, allow_null=True, allow_blank=True)

    def validate_file_url(self, value):
        if value:
            parsed_url = urllib.parse.urlparse(value)
            if not all([parsed_url.scheme, parsed_url.netloc]):
                raise serializers.ValidationError("Invalid URL format.")

            encoded_url = urllib.parse.quote(value, safe=':/')
            print("Validating file URL:", encoded_url)
            return encoded_url
        return value
