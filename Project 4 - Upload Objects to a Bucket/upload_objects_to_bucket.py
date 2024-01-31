# Import required libraries
import os
import boto3
import sys

# Upload all files from a local directory to S3 bucket
def upload_all_files_to_s3(bucket_name, region, local_directory):
    s3 = boto3.client('s3', region_name=region)

    try:
        for root, dirs, files in os.walk(local_directory):
            for file in files:
                local_file_path = os.path.join(root, file)
                
                # Use relative path as S3 key
                s3_key = os.path.relpath(local_file_path, local_directory)
                
                response = s3.upload_file(local_file_path, bucket_name, s3_key)
                print(f"File '{local_file_path}' uploaded to '{bucket_name}' with key '{s3_key}'")

        print("All files uploaded successfully.")
        return response
    except Exception as e:
        print(f"Error uploading files: {e}")
        return None

# Check if command line arguments are provided
if len(sys.argv) < 4:
    print("Usage: python upload-all-to-s3.py <bucket_name> <region> <local_directory>")
    sys.exit(1)

# Assign command line values to variables
bucket_name = sys.argv[1]
region = sys.argv[2]
local_directory = sys.argv[3]

# Call the function to upload all files from the directory
upload_all_files_to_s3(bucket_name, region, local_directory)
