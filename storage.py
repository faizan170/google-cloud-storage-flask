'''
All these methods belong to google storage python client repo.
'''

# Imports the Google Cloud client library
from google.cloud import storage
from google.oauth2 import service_account
# Instantiates a client

# Added service account
storage_client = storage.Client.from_service_account_json('app-devfever-c5f74595fdd8.json')

def create_bucket(bucket_name = "checkma"):
    """Creates a new bucket."""
    try:
        bucket = storage_client.create_bucket(bucket_name)
        print('Bucket {} created'.format(bucket.name))
        return True
    except:
        return False

def upload_blob(source_file_name, destination_blob_name, bucket_name = "checkma"):
    """Uploads a file to the bucket."""
    try:
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)

        blob.upload_from_filename(source_file_name)

        print('File {} uploaded to {}.'.format(
            source_file_name,
            destination_blob_name))
        return True
    except:
        return False


def download_blob(source_blob_name, destination_file_name, bucket_name = "checkma"):
    """Downloads a blob from the bucket."""
    try:
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(source_blob_name)

        blob.download_to_filename(destination_file_name)

        print('Blob {} downloaded to {}.'.format(
            source_blob_name,
            destination_file_name))
        return True
    except:
        return False

def delete_blob(blob_name, bucket_name = "checkma"):
    """Deletes a blob from the bucket."""
    try:
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(blob_name)

        blob.delete()

        print('Blob {} deleted.'.format(blob_name))
    except:
        return False


def list_blobs(parent="", bucket_name = "checkma"):
    """Lists all the blobs in the bucket."""
    try:
        # Note: Client.list_blobs requires at least package version 1.17.0.
        blobs = storage_client.list_blobs(bucket_name, prefix=parent)
        listData = []
        for blob in blobs:
            listData.append(blob.name.replace(parent, ""))
        return listData
    except:
        return False

def create_folder(path, bucket_name = "checkma"):
    """ Create a new folder """
    try:
        bucket = storage_client.get_bucket(bucket_name)
        if path[-1] != "/":
            path += "/"
        blob = bucket.blob(path)

        blob.upload_from_string('', content_type='application/x-www-form-urlencoded;charset=UTF-8')
        return True
    except:
        return False


def delete_folder(path, bucket_name = "checkma"):
    """ Delete a folder """
    try:
        if path[-1] != "/":
            path += "/"
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(path)

        blob = bucket.blob(path)

        blob.delete()

        print('Blob {} deleted.'.format(path))
    except:
        return False

def check_folder_exists(folderPath, bucket_name="checkma"):
    """ check if path/file exists in bucket or not in google storage """
    bucket = storage_client.bucket(bucket_name)
    stats = storage.Blob(bucket=bucket, name=folderPath).exists(storage_client)
    return stats

