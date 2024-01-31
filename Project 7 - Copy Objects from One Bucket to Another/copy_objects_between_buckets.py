# Import required libraries
import boto3
import sys

# Copy all objects from source bucket to destination bucket
def copy_objects_between_buckets(region, source_bucket, destination_bucket):
    s3 = boto3.client('s3', region_name=region)

    try:
        response = s3.list_objects_v2(Bucket=source_bucket)

        if 'Contents' in response:
            objects = response['Contents']
            
            # Copy each object to the destination bucket
            for obj in objects:
                copy_source = {'Bucket': source_bucket, 'Key': obj['Key']}
                destination_key = obj['Key']  # You can modify this if you want to rename the objects in the destination bucket
                
                s3.copy_object(CopySource=copy_source, Bucket=destination_bucket, Key=destination_key)
                print(f"Copied object: {obj['Key']}")

        print(f"All objects copied from '{source_bucket}' to '{destination_bucket}' in '{region}'.")
    except Exception as e:
        print(f"Error copying objects between buckets: {e}")

# Check if command line arguments are provided
if len(sys.argv) < 4:
    print("Usage: python copy_objects_between_buckets.py <region> <source_bucket> <destination_bucket>")
    sys.exit(1)

# Assign command line values to variables
region = sys.argv[1]
source_bucket = sys.argv[2]
destination_bucket = sys.argv[3]

# Call the function to copy objects between buckets
copy_objects_between_buckets(region, source_bucket, destination_bucket)
