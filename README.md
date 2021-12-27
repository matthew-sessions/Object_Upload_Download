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
* **hostname** - https://<host name from vultr>
* **access_key_id** - access key from vultr
