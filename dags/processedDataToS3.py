from fetchTransformRawData import transformData
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
import datetime
import json

def uploadProcessedData() -> None:

    processedData = transformData() #import the transformed, flattened data
    processedData = json.dumps(processedData) #JSON format

    s3Hook = S3Hook()

    s3BucketName = "chi-processed-data"
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S") #append current datetime to file name for record/version purposes
    newS3Key = f"chi-processed-data-{timestamp}"

    try:
        s3Hook.load_string(processedData,key=newS3Key, bucket_name=s3BucketName) #push to processed data bucket
        print(f"Processed data upload to s3 bucket {s3BucketName} successful")
    except Exception as e:
        print(f"Error on upload instance: {e}")
