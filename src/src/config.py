from dotenv import load_dotenv
import os


load_dotenv()



OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
S3_BUCKET_NAME = os.getenv('S3_BUCKET_NAME')
S3_ACCESS_KEY = os.getenv('S3_ACCESS_KEY')
S3_SECRET_KEY = os.getenv('S3_SECRET_KEY')
S3_REGION = os.getenv('S3_REGION')

print(os.getenv('PORT'))