import boto3
import json
import sys

# Create and apply a bucket policy
def create_and_apply_bucket_policy(region, bucket_name):
    s3 = boto3.client('s3', region_name=region)

    # Define a simple bucket policy JSON
    bucket_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": [
                "s3:GetObject",
            ],
            "Resource": [
                f"arn:aws:s3:::{bucket_name}",
                f"arn:aws:s3:::{bucket_name}/*"
            ]
        }
    ]
}


    try:
        # Convert the policy to a JSON string
        policy_json = json.dumps(bucket_policy)

        # Apply the bucket policy
        s3.put_bucket_policy(Bucket=bucket_name, Policy=policy_json)

        print(f"Bucket policy applied to '{bucket_name}'.")
    except Exception as e:
        print(f"Error creating and applying bucket policy: {e}")

# Check if command line arguments are provided
if len(sys.argv) < 3:
    print("Usage: python create_bucket_policy.py <region> <bucket_name>")
    sys.exit(1)

# Assign command line values to variables
region = sys.argv[1]
bucket_name = sys.argv[2]

# Call the function to create and apply the bucket policy
create_and_apply_bucket_policy(region, bucket_name)
