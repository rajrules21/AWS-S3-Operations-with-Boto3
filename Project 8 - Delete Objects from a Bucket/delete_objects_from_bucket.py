
#import required libraries
import boto3
import sys


# Delete all objects in S3 bucket
def delete_all_objects_in_bucket(region, bucket_name):
    s3 = boto3.client('s3', region_name=region)

    try:
        response = s3.list_objects_v2(Bucket=bucket_name)

        if 'Contents' in response:
            objects = response['Contents']
            
            # Delete each object
            for obj in objects:
                s3.delete_object(Bucket=bucket_name, Key=obj['Key'])
                print(f"Deleted object: {obj['Key']}")

        print(f"All objects deleted from S3 Bucket '{bucket_name}' in '{region}'.")
    except Exception as e:
        print(f"Error deleting objects in bucket: {e}")
        
        
#check if command line arguments are provided
if len(sys.argv) < 3:
    print("Usage: python delete_all_objects_in_bucket.py <region> <bucket_name>")
    sys.exit(1)
    
#Assign command line values to variables
region = sys.argv[1]
bucket_name = sys.argv[2]
        
# Call the function to delete all objects
delete_all_objects_in_bucket(region, bucket_name)