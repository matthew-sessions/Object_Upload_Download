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

# If a bucket does not exsists it can be created
# with this command
client.create_bucket(Bucket="test_bucket")

# The names of the pictures in "photos_to_upload" folder
# can be stored in a list like this
picture_names = os.listdir("photos_to_upload")

# Iterate through the pic names and store to Object Storage
for pic_name in picture_names:
    # this is the path of the pictures being read from disk
    picture_path = f"photos_to_upload/{pic_name}"
    # you can store a picture in a folder within a bucket
    # by adding a path before a the picture name
    pic_to_store_name = f"test_folder/{pic_name}"
    # this is the command to updload a picture
    client.upload_file(
        Filename=picture_path, Bucket="test_bucket", Key=pic_to_store_name
    )
