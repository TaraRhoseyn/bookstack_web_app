import os
import boto3
from flask import request
from botocore.exceptions import ClientError
from werkzeug.utils import secure_filename

# AWS creds
client = boto3.client('s3',
                      aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"),
                      aws_secret_access_key=os.environ.get
                      ("AWS_SECRET_ACCESS_KEY"))
