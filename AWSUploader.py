import os
import boto3
from botocore.exceptions import NoCredentialsError
from dotenv import load_dotenv

load_dotenv()


  
     
 
def upload_to_s3(local_path, bucket_name, s3_path):
    s3 = boto3.client(
        's3',
        aws_access_key_id=os.getenv('accessKeyId'),
        aws_secret_access_key=os.getenv('secretAccessKey'),
    )
    for root, dirs, files in os.walk(local_path):
        for file in files:
            local_file_path = os.path.join(root, file)
            s3_file_path = os.path.join(s3_path, os.path.relpath(local_file_path, local_path))
            try:
                # Verifica se local_file_path è un file prima di caricare
                if os.path.isfile(local_file_path):
                    s3_file_path=s3_file_path.replace('\\','/')
                    s3.upload_file(local_file_path, bucket_name, s3_file_path)
                    print(f"File '{local_file_path}' caricato su S3 come '{s3_file_path}'.")
                else:
                    print(f"Ignorato '{local_file_path}' perché è una directory.")
            except NoCredentialsError:
                print("Le credenziali AWS non sono configurate correttamente o mancanti.")
                return False
    return True


def runner():
    local_path = "./public"
    bucket_name = os.getenv('bucket_name')
    s3_path = "public/"

    if upload_to_s3(local_path, bucket_name, s3_path):
        print(f"Tutti i file in {local_path} sono stati caricati su S3 nel percorso {s3_path}.")
    else:
        print("Caricamento su S3 non riuscito.")

runner()