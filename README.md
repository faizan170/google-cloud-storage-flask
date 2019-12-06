# Google Cloud Storage Flask
Google cloud storage operations in Python with flask. You can perform these operations with this application for your cloud storage.
* Create folder
* Create/Upload file
* Delete folder/file
* Get all data
### To use
Install requirements file
```
pip install -r requirements.txt
```

Go to [https://cloud.google.com/docs/authentication/getting-started](https://cloud.google.com/docs/authentication/getting-started) to create google cloud
credentials key. Download key and set path to key using
```
set GOOGLE_APPLICATION_CREDENTIALS = PATH_TO_KEY
```

To run server
```
python main.py
```
