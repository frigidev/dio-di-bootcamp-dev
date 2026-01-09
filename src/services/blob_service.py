import os
import streamlit as st
from azure.storage.blob import BlobServiceClient
from utils.Config import Config

def upload_blob(file, file_name):
    try:
        # Validar se as variáveis de ambiente estão definidas
        if not Config.STORAGE_CONNECTION_STRING:
            st.error("Erro: STORAGE_CONNECTION_STRING não está definida. Verifique o arquivo .env")
            return None
        
        if not Config.CONTAINER_NAME:
            st.error("Erro: CONTAINER_NAME não está definida. Verifique o arquivo .env")
            return None
        
        blob_service_client = BlobServiceClient.from_connection_string(Config.STORAGE_CONNECTION_STRING)
        blob_client = blob_service_client.get_blob_client(container=Config.CONTAINER_NAME, blob=file_name)
        blob_client.upload_blob(file, overwrite=True)
        return blob_client.url
    except Exception as e:
        st.error(f"Erro ao enviar o arquivo para o Azure Blob Storage: {e}")
        return None