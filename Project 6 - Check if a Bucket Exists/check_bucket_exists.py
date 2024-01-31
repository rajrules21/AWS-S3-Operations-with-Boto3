import boto3
import sys
from botocore.exceptions import ClientError

# Check if an S3 bucket exists
def check_bucket_exists(region, bucket_name):
    s3 = boto3.client('s3', region_name=region)

    try:
        # Head the bucket to check if it exists
        s3.head_bucket(Bucket=bucket_name)
        print(f"The bucket '{bucket_name}' exists in '{region}'.")
        return True

    except ClientError as e:
        if e.response['Error']['Code'] == '404':
            print(f"The bucket '{bucket_name}' does not exist in '{region}'.")
            return False
        else:
            print(f"Error checking bucket existence: {e}")
            return False

# Check if command line arguments are provided
if len(sys.argv) < 3:
    print("Usage: python check_bucket_exists.py <region> <bucket_name>")
    sys.exit(1)

# Assign command line values to variables
region = sys.argv[1]
bucket_name = sys.argv[2]

# Call the function to check if the bucket exists
check_bucket_exists(region, bucket_name)
