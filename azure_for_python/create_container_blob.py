#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 스토리지 연결 문자열 구성
# Linux: export AZURE_STORAGE_CONNECTION_STRING="<yourconnectionstring>"

import sys, os, uuid # if not install azure-storage-blob, please run command "sudo pip3 install azure-storage-blob" :
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__
connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
local_path = "/home/azureuser"
local_file_name = "ls" + ".sh"

try:
    print("Azure Blob storage v" + __version__ + " - Python quickstart sample")
    # Create the BlobServiceClient object which will be used to create a container client
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    # container_name = "sample" + str(uuid.uuid4())
    container_name = "samplecontainer"
    # print("container_name: %s" % container_name)
    all_containers = blob_service_client.list_containers()
    for container in all_containers:
        if (container['name'] == container_name):
            container_name = "container" + str(uuid.uuid4())
            container_client = blob_service_client.create_container(container_name)
            upload_file_path = os.path.join(local_path, local_file_name)
            blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)
            print("\nUploading to Azure Storage as blob:\n\t" + local_file_name)
            with open(upload_file_path, "rb") as data:
                blob_client.upload_blob(data)
        # else:
        #     container_client = blob_service_client.create_container(container_name)
        #     print(container_name)
        #     upload_file_path = os.path.join(local_path, local_file_name)
        #     blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)
        #     print("\nUploading to Azure Storage as blob:\n\t" + local_file_name)
        #     with open(upload_file_path, "rb") as data:
        #         blob_client.upload_blob(data)
except Exception as ex:
    print(ex)
