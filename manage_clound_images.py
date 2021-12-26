import os
import shutil
import boto3
import decouple
import concurrent.futures
import time


class ImageManager:
    session = None
    client = None

    def __init__(
        self,
        hostname: str,
        access_key_id: str,
        secret_access_key: str,
        tmp_folder_path: str,
        storage_folder_path: str,
        cam_id: str,
    ):
        self.hostname = hostname
        self.access_key_id = access_key_id
        self.secret_access_key = secret_access_key
        self.cam_id = cam_id
        self.tmp_folder_path = tmp_folder_path
        self.storage_folder_path = storage_folder_path
        self.images_to_process = set()
        self.processed_images = set()
        self.buckets = set()

    def create_client(self):
        self.session = boto3.session.Session()
        self.client = self.session.client(
            "s3",
            endpoint_url=hostname,
            aws_access_key_id=access_key_id,
            aws_secret_access_key=secret_access_key,
        )

    def maybe_create_bucket(self, bucket_name: str):
        if bucket_name not in self.buckets:
            self.client.create_bucket(Bucket=bucket_name)

    def scan_new_images(self):
        for image in os.listdir(self.tmp_folder_path):
            if image not in self.processed_images:
                self.images_to_process.add(image)

    def move_file_to_storage(self, filename):
        try:
            print("Moved file: ", filename)
            shutil.move(
                f"{self.tmp_folder_path}/{filename}",
                f"{self.storage_folder_path}/{filename}",
            )
            print("Moved file final: ", filename)
        except:
            print("File move issue")

    def upload_and_move(self, filename: str):
        bucket_name = self.parse_bucket_name(filename)
        print(f"Maybe create bucket", bucket_name)
        self.maybe_create_bucket(bucket_name)
        self.client.upload_file(
            Filename=f"{self.tmp_folder_path}/{filename}",
            Bucket=bucket_name,
            Key=filename,
        )
        print("Uploaded file: ", filename)
        self.move_file_to_storage(filename)
        self.processed_images.add(filename)
        if filename in self.images_to_process:
            self.images_to_process.remove(filename)

    def parse_bucket_name(self, filename: str):
        return f"{self.cam_id}_{filename.split('_')[0]}"

    def thread_upload(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
            img_list = list(self.images_to_process)
            res = executor.map(self.upload_and_move, img_list)


    def run(self):
        while True:
            print("Sleeping")
            time.sleep(2)
            self.scan_new_images()
            if len(self.images_to_process) > 0:
                self.thread_upload()
            else:
                print("No images to process")


if __name__ == "__main__":
    hostname = decouple.config("hostname")
    access_key_id = decouple.config("access_key_id")
    secret_access_key = decouple.config("secret_access_key")
    tmp_path = decouple.config("tmp_path")
    store_path = decouple.config("store_path")
    cam_id = decouple.config("cam_id")
    image_manager = ImageManager(
        hostname=hostname,
        access_key_id=access_key_id,
        secret_access_key=secret_access_key,
        tmp_folder_path=tmp_path,
        storage_folder_path=store_path,
        cam_id=cam_id,
    )
    image_manager.create_client()
    image_manager.run()
