# Pi Image Manager

## Getting Started
### Step 1
Turn on the Pi and cd into the directory that you want this application to live. Then run the following command:
```git clone https://github.com/matthew-sessions/Pi_Image_Managers.git```

### Step 2
cd into Pi_Image_Managers

### Step 3
You will want to edit the .env file. You can do so by running the following:
```nano .env```
Then add the listed values below:
```
hostname=https://ewr1.vultrobjects.com
access_key_id=ACCESS_KEY
secret_access_key=SECRET_KEY
tmp_path=/path/to/tmp
store_path=/path/to/store
cam_id=cam_id
```
#### Info about the env variables:
* **hostname** - https://<host name from vultr>
* **access_key_id** - access key id from vultr
* **secret_access_key** - secret access key from vultr
* **tmp_path** - the path the folder where images will be stored temporarily (at the end of the path make sure there is no **/**)
* **store_path** - the path the folder where images will be stored for the long term (at the end of the path make sure there is no **/**)
* **cam_id** - This is the ID you assign to the Pi. This will allow you to know which Pi took what photos.
  
### Step3
Install the python deps with the following command:
```pip3 install -r base.txt```
  
### Step 4
Run the application that uploads images to the cloud:
```python3 upload_cloud_images.py```
  
  ![](https://github.com/matthew-sessions/Pi_Image_Managers/blob/main/design.png "")
