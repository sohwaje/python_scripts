#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Linux: export AZURE_STORAGE_CONNECTION_STRING="<yourconnectionstring>"
# if not install azure-storage-blob, please run command "sudo pip3 install azure-storage-blob"
"""
Azure blob 컨테이너에 Blob(모든 로컬 파일, 디렉토리)을 컨테이너에 업로드한다.
"""
import sys, os, uuid, glob
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__

"""
변수 설정
"""
# azure blob 스토리지 연결
connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
# 로컬 경로(업로드 대상들이 있음)
local_path = "/home/azureuser/"
# 업로드 경로: azure blob container(이미 생성되어 있어야 함)
upload_container_name = "hiclass"

"""
파일 리스트와 디렉토리 리스트를 구하는 함수.
"""
def get_list_local(local_path, files = [], directories = []):
    for file in os.listdir(local_path):
        item = local_path + file                                # item은 path+file 명으로 설정
        if os.path.isdir(item):                                 # item이 디렉토리인지 파일인지 확인.
            directories.append(item + "/")                      # item이 디렉토리면, directories 리스트에 추가.
            get_list_local(item + "/", files, directories)      # item이 디렉토리면, 하위디렉토리까지 탐색.
        else :
            files.append(item)
    return files, directories

"""
업로드 함수
"""
def upload_file():
    files, directories = get_list_local(local_path) # 파일 목록과 디렉토리 목록을 구함
    for file in files:
        upload_path = file.replace(local_path,"").replace("/","/")  # 파일 경로를 절대 경로에서 상대 경로로 바꿈.
        upload_file_path = os.path.join(upload_path)
        blob_client = blob_service_client.get_blob_client(container=upload_container_name, blob=upload_file_path)
        print("\nUploading to Azure Storage as blob:\n\t" + file)
        with open(upload_file_path, "rb") as data:
            blob_client.upload_blob(data)

try:
    print("Azure Blob storage v" + __version__ + " - Python quickstart")
    # 컨테이너 클라이언트를 만드는 데 사용할 blob서비스 클라이언트 오브젝트를 생성한다.
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    container_list=[]
    all_containers = blob_service_client.list_containers()          # 모든 컨테이너 리스트를 구함.
    for container in all_containers:                                # 모든 컨테이너에서 생성할 컨테이너를 찾음
        container_list.append(container['name'])                    # 컨테이너 리스트에 해당 컨테이너를 추가
    if upload_container_name not in container_list:
        print("upload_container_name : " + upload_container_name + " dose not exist.")
        sys.exit()
    else:
        print("upload_container_name : " + upload_container_name + " dose exist.")
        upload_file()
except Exception as ex:
    print(ex)
