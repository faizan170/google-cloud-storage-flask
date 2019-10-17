from google.cloud.storage import Client
creds_file = 'app-devfever-c5f74595fdd8.json'
client = Client.from_service_account_json(creds_file)
print(list(client.list_buckets()))