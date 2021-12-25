import boto3
import os



# Create a session for fast upbloads
session = boto3.session.Session()
# Create a client to interface with objects/buckets
client = session.client(
    "s3",
    endpoint_url=hostname,
    aws_access_key_id=access_key_id,
    aws_secret_access_key=secret_access_key,
)

# iterate through file info within a bucket
for key in client.list_objects(Bucket="test_bucket", Prefix="test_folder")["Contents"]:
    # parse file name from the key
    filename = key["Key"]
    print(f"Saving {filename}")
    client.download_file(
        Bucket="test_bucket", Key=filename, Filename=f"downloaded_photos/{filename}"
    )
