import boto3
import sys

# Get S3 URL for a bucket
def get_bucket_url(region, bucket_name):
    return f"https://{bucket_name}.s3.{region}.amazonaws.com/"

# List S3 URLs for all objects in a bucket
def list_object_urls(region, bucket_name):
    s3 = boto3.client('s3', region_name=region)

    try:
        response = s3.list_objects_v2(Bucket=bucket_name)

        if 'Contents' in response:
            objects = response['Contents']

            for obj in objects:
                object_key = obj['Key']
                object_url = get_bucket_url(region, bucket_name) + object_key
                print(f"Object URL: {object_url}")

    except Exception as e:
        print(f"Error listing object URLs: {e}")

# Check if command line arguments are provided
if len(sys.argv) < 3:
    print("Usage: python list_s3_urls.py <region> <bucket_name>")
    sys.exit(1)

# Assign command line values to variables
region = sys.argv[1]
bucket_name = sys.argv[2]

# Print S3 URL for the bucket
bucket_url = get_bucket_url(region, bucket_name)
print(f"Bucket URL: {bucket_url}")

# List S3 URLs for all objects in the bucket
list_object_urls(region, bucket_name)
