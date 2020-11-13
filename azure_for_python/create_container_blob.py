#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Linux: export AZURE_STORAGE_CONNECTION_STRING="<yourconnectionstring>"
# if not install azure-storage-blob, please run command "sudo pip3 install azure-storage-blob"
import sys, os, uuid, glob
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__

connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
local_path = "/home/azureuser"
local_file_name = "ls" + ".sh"

def Create_container_and_upload_file():
    upload_file_path = os.path.join(local_path, local_file_name)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)
    print("\nUploading to Azure Storage as blob:\n\t" + local_file_name)
    with open(upload_file_path, "rb") as data:
        blob_client.upload_blob(data)

try:
    print("Azure Blob storage v" + __version__ + " - Python quickstart sample")
    # Create the BlobServiceClient object which will be used to create a container client
    # 컨테이너 클라이언트를 만드는 데 사용할 blob서비스 클라이언트 오브젝트를 생성한다.
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    container_name = "samplecontainer"
    container_list=[]
    all_containers = blob_service_client.list_containers()
    for container in all_containers:
        container_list.append(container['name'])
    if container_name not in container_list:
        print("container_name : " + container_name + " dose not exist.")
        container_client = blob_service_client.create_container(container_name)
        Create_container_and_upload_file()
    else:
        print("container_name : " + container_name + " dose exist.")
        container_name = "sample" + str(uuid.uuid4())
        print("new container_name : " + container_name)
        container_client = blob_service_client.create_container(container_name)
        Create_container_and_upload_file()
except Exception as ex:
    print(ex)
