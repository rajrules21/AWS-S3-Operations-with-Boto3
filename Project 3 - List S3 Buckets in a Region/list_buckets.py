#import required libraries
import boto3
import sys


#list s3 buckets
def list_s3_buckets(region):
    s3 = boto3.client('s3', region_name=region)
    
    try:
        response = s3.list_buckets()
        buckets = response['Buckets']
        
        print(f"S3 Buckets in {region} region: ")
        for bucket in buckets:
            print(f" - {bucket["Name"]}")
            
    except Exception as e:
        print(f" Error listing buckets: {e}")
        
#check if command line arguments are provided
if len(sys.argv) < 2:
    print("Usage: python list_buckets.py <region>")
    sys.exit(1)
    
#Assign command line values to variables
region = sys.argv[1]
        
#call the function
list_s3_buckets(region)
        
   



