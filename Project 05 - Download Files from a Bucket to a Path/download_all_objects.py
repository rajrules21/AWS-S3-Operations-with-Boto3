import boto3
import sys
import os
from botocore.exceptions import NoCredentialsError

# Download all objects from an S3 bucket
def download_all_objects(region, bucket_name, local_path):
    s3 = boto3.client('s3', region_name=region)

    try:
        response = s3.list_objects_v2(Bucket=bucket_name)

        if 'Contents' in response:
            objects = response['Contents']

            for obj in objects:
                object_key = obj['Key']
                download_path = os.path.join(local_path, object_key)

                # Download the object
                s3.download_file(bucket_name, object_key, download_path)
                print(f"Object '{object_key}' downloaded to '{download_path}'")

        print(f"All objects from '{bucket_name}' downloaded to '{local_path}'.")
    except NoCredentialsError:
        print("Credentials not available. Please configure your AWS credentials.")
    except Exception as e:
        print(f"Error downloading objects: {e}")

# Check if command line arguments are provided
if len(sys.argv) < 4:
    print("Usage: python download_all_objects.py <region> <bucket_name> <local_path>")
    sys.exit(1)

# Assign command line values to variables
region = sys.argv[1]
bucket_name = sys.argv[2]
local_path = sys.argv[3]

# Call the function to download all objects
download_all_objects(region, bucket_name, local_path)
