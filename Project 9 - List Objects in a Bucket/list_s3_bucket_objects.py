#import required libraries
import boto3
import sys


#list s3 buckets
def list_s3_bucket_objects(region, bucket_name):
    s3 = boto3.client('s3', region_name=region)
    
    try:
        response = s3.list_objects_v2(Bucket=bucket_name)
        
        if 'Contents' in response:
            objects = response['Contents']
        
            print(f"Objects in S3 Bucket '{bucket_name}' in '{region}': ")
            for obj in objects:
                print(f" - {obj['Key']}")
        else:
            print(f"No objects found in bucket '{bucket_name}' ")
            
    except Exception as e:
        print(f" Error listing objects in buckets: {e}")
        
#check if command line arguments are provided
if len(sys.argv) < 3:
    print("Usage: python list_s3_bucket_objects.py <region> <bucket_name>")
    sys.exit(1)
    
#Assign command line values to variables
region = sys.argv[1]
bucket_name = sys.argv[2]
        
#call the function
list_s3_bucket_objects(region, bucket_name)
        
   



