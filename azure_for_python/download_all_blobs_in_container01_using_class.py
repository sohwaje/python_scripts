# ref: https://www.quickprogrammingtips.com/azure/how-to-download-blobs-from-azure-storage-using-python.html
# ** Requires python 3.6 or above **
# pip3 install azure-storage-blob --user

# -*- coding: utf-8 -*-
import os
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__

# azure blob 스토리지 연결문자열
connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
# 다운로드 받을 디렉토리 경로
LOCAL_BLOB_PATH = "D:\TEST_DOWNLOAD"
# 블롭 컨테이너 이름
BLOB_CONTAINER = "testapibuild"


class AzureBlobFileDownloader:
    def __init__(self):
        # blob 컨테이너에 연결하기 위한 클래스
        self.blob_service_client = BlobServiceClient.from_connection_string(
            connect_str)
        self.container_client = self.blob_service_client.get_container_client(
            BLOB_CONTAINER)
        # blob을 저장하기 위한 함수

    def save_blob(self, file_name, file_content):
        download_file_path = os.path.join(
            LOCAL_BLOB_PATH, file_name)   # 경로: /LOCAL_BLOB_PATH/file_name
        # blob의 디렉토리 구조 동일한 구조를 생성한다.
        os.makedirs(os.path.dirname(download_file_path),
                    exist_ok=True)  # 하위 디렉토리까지 생성
        # download_file_path를 쓰기 모드로 열고 file이라는 별칭으로 치환한다.
        with open(download_file_path, "wb") as file:
            # file에 file_content(블롭의 내용)을 쓴다.
            file.write(file_content)
        """
        ex) with open("foo.txt", "w") as f:
                f.write("Life is too short, you need python")
        """

    def download_all_blobs_in_container(self):
        # blob의 리스트가 있는 my_blobs 인스턴스 생성
        my_blobs = self.container_client.list_blobs()
        print("my_blobs:", my_blobs)
        for blob in my_blobs:                               # my_blobs 인스턴스에서 blob을 하나씩 꺼냄
            print(blob.name)
            # blob의 콘텐츠를 하나하나 읽어 메모리에 저장한다
            bytes = self.container_client.get_blob_client(
                blob).download_blob().readall()
            self.save_blob(blob.name, bytes)  # 블롭의 이름과 블롭의 내용


go_download = AzureBlobFileDownloader()  # Class를 객체화 한다
go_download.download_all_blobs_in_container()
