
# import boto3

# # Create a Boto3 S3 client
# s3_client = boto3.client('s3')

# # List all S3 buckets
# response = s3_client.list_buckets()

# # Print the names of the buckets
# for bucket in response['Buckets']:
#     print(bucket['Name'])



# uploading a file to bucket
import boto3

# Create a Boto3 S3 client
s3_client = boto3.client('s3')

# Upload an image file to the bucket
file_path = '/home/afthash/Desktop/test/2023-08-17/downloaded_image.jpg'
bucket_name = 'my-random-bucket-12345'
object_key = 'downloaded_image.jpg'

s3_client.upload_file(file_path, bucket_name, object_key)

print(f"Image uploaded to S3 bucket: {bucket_name}")


