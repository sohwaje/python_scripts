import re, sys, os, uuid, glob
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__

"""
변수 설정
"""
# azure blob 스토리지 연결
connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
# 로컬 파일 경로
LOCAL_BLOB_PATH = "/Users/yusunglee/Downloads/slack"
# 업로드 경로: azure blob container
BLOB_CONTAINER = "testapibuild"

# blob 스토리지 연결 문자열을 통해 blob에 접근하는 인스턴스 생성
blob_service_client = BlobServiceClient.from_connection_string(connect_str)
container_client = blob_service_client.get_container_client(BLOB_CONTAINER)
"""
blob 리스트 구하는 함수
"""
def get_list_all_blob_in_container():
    blob_list = container_client.list_blobs()
    return blob_list

"""
저장 함수
"""
def save_blob(file_name,file_content):
    download_file_path = os.path.join(LOCAL_BLOB_PATH, file_name)
    os.makedirs(os.path.dirname(download_file_path), exist_ok=True)
    with open(download_file_path, "wb") as download_file:
        download_file.write(file_content)

"""
다운로드 함수
"""
def download_all_blobs_in_container():
    my_blobs = get_list_all_blob_in_container()
    print("my_blobs: ", my_blobs)
    for blob in my_blobs:
        print(blob.name)
        bytes = container_client.get_blob_client(blob).download_blob().readall()
        save_blob(blob.name, bytes) # blob.name = blob 이름, bytes = blob 내용


download_all_blobs_in_container()
