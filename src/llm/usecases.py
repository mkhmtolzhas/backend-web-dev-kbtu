from openai import OpenAI
from src.config import OPENAI_API_KEY

class LLMUseCase:
    def __init__(self, api_key: str):
        self.openai = OpenAI(api_key=api_key)

    def generate_response(self, prompt: str) -> str:
        response = self.openai.responses.create(
            model="gpt-4o",
            instructions="You are a helpful assistant.",
            input=prompt,
        )

        return response.output_text
    
    def generate_response_from_file(self, prompt: str, file_url: str) -> str:
        response = self.openai.responses.create(
            model="gpt-4o",
            input=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "input_image",
                            "image_url": file_url,
                        }
                    ]
                }
            ]

        )

        return response.output_text
    

llm_use_case = LLMUseCase(api_key=OPENAI_API_KEY)