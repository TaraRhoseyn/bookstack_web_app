import os
import boto3
from flask import Flask, request
from botocore.exceptions import ClientError
from werkzeug.utils import secure_filename

# AWS variables
s3_bucket = "ci-ms3-bookstack"
bucket_url = "https://ci-ms3-bookstack.s3.eu-west-2.amazonaws.com/"
# AWS creds
client = boto3.client('s3',
                      aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"),
                      aws_secret_access_key=os.environ.get
                      ("AWS_SECRET_ACCESS_KEY"))

def store_image(img_to_store: str) -> str:
    """
    This function stores user-inputted
    image file into an AWS s3 bucket.
    """
    img = request.files[img_to_store]
    img_file = secure_filename(img.filename)
    try:
        s3 = boto3.resource('s3')
        s3.Bucket(s3_bucket).put_object(Key=img_file, Body=img)
    except ClientError:
        raise Exception("The image cannot be uploaded to the AWS S3 bucket.")
    img_path = bucket_url + img_file
    return img_path