import boto3
from django.conf import settings


def delete_from_s3(filename):
    s3 = boto3.client(
        "s3",
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
    )
    s3.delete_object(Bucket=settings.AWS_STORAGE_BUCKET_NAME, Key=filename)
