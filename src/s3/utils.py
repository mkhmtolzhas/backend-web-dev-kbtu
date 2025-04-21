import boto3
from src.config import S3_ACCESS_KEY, S3_SECRET_KEY, S3_REGION, S3_BUCKET_NAME


def upload_file_to_s3(file_obj, filename, content_type):
    s3 = boto3.client(
        's3',
        aws_access_key_id=S3_ACCESS_KEY,
        aws_secret_access_key=S3_SECRET_KEY,
        region_name=S3_REGION,
    )

    s3.upload_fileobj(
        file_obj,
        S3_BUCKET_NAME,
        f'uploads/{filename}',
        ExtraArgs={'ContentType': content_type, 'ACL': 'public-read'}
    )

    return f'https://{S3_BUCKET_NAME}.s3.amazonaws.com/uploads/{filename}'
