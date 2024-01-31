# AWS S3 Operations with Python and Boto3

This project focuses on performing various operations on Amazon Simple Storage Service (S3) using Python and the Boto3 library. The goal is to provide a set of subprojects that cover essential S3 tasks, allowing users to interact with S3 buckets and objects programmatically.

## Overview

Amazon S3 is a scalable object storage service that allows you to store and retrieve any amount of data. This project leverages the Boto3 library, the official Python SDK for AWS, to automate various S3 operations.

## Sub-Projects

1. **Create S3 Bucket:**
   - Python script to create a new S3 bucket.

2. **Delete S3 Bucket:**
   - Python script to delete an existing S3 bucket.

3. **List S3 Buckets in a Region:**
   - Python script to list all S3 buckets in a specified region.

4. **Upload Objects to a Bucket:**
   - Python script for uploading objects to an S3 bucket.

5. **Download Files from a Bucket to a Path:**
   - Python script for downloading files from an S3 bucket to a local path.

6. **Check if a Bucket Exists:**
   - Python script to check if a specific S3 bucket already exists.

7. **Copy Objects from One Bucket to Another:**
   - Python script for copying objects from one S3 bucket to another.

8. **Delete Objects from a Bucket:**
   - Python script to delete objects from an S3 bucket.

9. **List Objects in a Bucket:**
   - Python script to list all objects in a specified S3 bucket.

10. **List S3 URL for All Objects in a Bucket:**
    - Python script to list S3 URLs for all objects in a specified S3 bucket.

11. **Disable Public Access Block for a Bucket:**
    - Python script to disable the public access block for a specific S3 bucket.

12. **Create and Apply Bucket Policy:**
    - Python script to create and apply a bucket policy for access control.


## Note:- Due to constant upgrades and changes to S3 from AWS, some files may not work and will need to be modified over a period of time.
 

## Usage

Navigate to the individual sub-projects' directories for detailed instructions on each operation:

## Usage

Navigate to the individual sub-projects' directories for detailed instructions on each operation:

- [Create S3 Bucket](Project_01_-_Create_S3_Bucket)
- [Delete S3 Bucket](Project_02_-_Delete_S3_Bucket)
- [List S3 Buckets in a Region](Project_03_-_List_S3_Buckets_in_a_Region)
- [Upload Objects to a Bucket](upload_objects/README.md)
- [Download Files from a Bucket to a Path](download_files/README.md)
- [Check if a Bucket Exists](check_bucket_exists/README.md)
- [Copy Objects from One Bucket to Another](copy_objects/README.md)
- [Delete Objects from a Bucket](delete_objects/README.md)
- [List Objects in a Bucket](list_objects/README.md)
- [List S3 URL for All Objects in a Bucket](list_urls/README.md)
- [Disable Public Access Block for a Bucket](disable_public_access_block/README.md)
- [Create and Apply Bucket Policy](bucket_policy/README.md)

## Prerequisites

Before using these scripts, ensure you have the following prerequisites:

- Python installed on your system.
- Boto3 library installed (`pip install boto3`).
- AWS credentials configured with the necessary permissions.


## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/aws-s3-python-boto3.git
   cd aws-s3-python-boto3


## Contributing

Contributions are welcome! If you have improvements or additional features you'd like to add, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

