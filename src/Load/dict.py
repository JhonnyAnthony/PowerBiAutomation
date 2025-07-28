import os
from dotenv import load_dotenv

load_dotenv('C:/Github/PowerBiAutomation/.env')

client_id = os.getenv('CLIENT_ID')
client_secret   = os.getenv('CLIENT_SECRET')
tenant_id = os.getenv('TENANT_ID')

group_id = os.getenv('WORKSPACE_ID')
dataset_id = os.getenv('DATASET_ID')

dict_extract = { 
    "Azure" : {
        'client_id': client_id,
        'client_secret': client_secret,
        'tenant_id': tenant_id,
        'workspace_id': group_id,
        'dataset_id': dataset_id
    }
}  