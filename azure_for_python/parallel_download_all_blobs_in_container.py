# download_blobs.py
# Python program to bulk download blob files from azure storage
# Uses latest python SDK() for Azure blob storage
# Requires python 3.6 or above
# pip3 install azure-storage-blob --user
import os
from multiprocessing.pool import ThreadPool
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__

CONNECTION_STRING = ""

# blob이 있는 컨테이너 이름
BLOB_CONTAINER = ""

# blob이 다운로드 될 디렉토리 경로
LOCAL_BLOB_PATH = ""


# Azure 스토리지 계정에 접근하기 위한 인스턴스
blob_service_client =  BlobServiceClient.from_connection_string(CONNECTION_STRING)
container_client = blob_service_client.get_container_client(BLOB_CONTAINER)


def download_all_blobs_in_container():
    my_blobs = container_client.list_blobs()
    result = run(my_blobs)
    print(result)

def run(blobs):
    with ThreadPool(processes=int(10)) as pool:
        return pool.map(save_blob_locally, blobs)

def save_blob_locally(blob):
    file_name = blob.name
    print(file_name)
    bytes = container_client.get_blob_client(blob).download_blob().readall() # blob을 읽어서 bytes 인스턴스에 넣는다.
    download_file_path = os.path.join(LOCAL_BLOB_PATH, file_name)   # /LOCAL_BLOB_PATH/file_name
    os.makedirs(os.path.dirname(download_file_path), exist_ok=True) # 하위 디렉토리까지 생성

    with open(download_file_path, "wb") as file:
      file.write(bytes) # bytes 인스턴스의 블롭을 쓴다
    return file_name

download_all_blobs_in_container()
