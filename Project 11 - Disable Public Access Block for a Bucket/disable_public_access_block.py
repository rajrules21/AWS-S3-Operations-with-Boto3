import boto3
import sys

# Disable block all public access for an S3 bucket
def disable_public_access_block(region, bucket_name, policy_value):
    s3 = boto3.client('s3', region_name=region)

    try:
        policy_value = policy_value.lower() == 'true'
        # Define the public access block configuration to disable all public access
        public_access_block_configuration = {
            'BlockPublicAcls': policy_value,
            'IgnorePublicAcls': policy_value,
            'BlockPublicPolicy': policy_value,
            'RestrictPublicBuckets': policy_value
        }

        # Apply the public access block configuration to the bucket
        s3.put_public_access_block(Bucket=bucket_name, PublicAccessBlockConfiguration=public_access_block_configuration)

        print(f"Block all public access disabled for S3 bucket '{bucket_name}'.")
    except Exception as e:
        print(f"Error disabling block all public access: {e}")

# Check if command line arguments are provided
if len(sys.argv) < 4:
    print("Usage: python disable_public_access.py <region> <bucket_name>")
    sys.exit(1)

# Assign command line values to variables
region = sys.argv[1]
bucket_name = sys.argv[2]
policy_value = sys.argv[3]



# Call the function to disable block all public access
disable_public_access_block(region, bucket_name, policy_value)
