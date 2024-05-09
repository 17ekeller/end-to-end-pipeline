from airflow.providers.amazon.aws.hooks.s3 import S3Hook
from rawDataExtract import rawExtractor
import datetime


def uploadRawData() -> None:
    rawData = rawExtractor()

    s3Hook = S3Hook()

    s3BucketName = "chi-weather-raw"
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S") #append current datetime to file name for record/version purposes
    newS3Key = f"chi-weather-raw-{timestamp}"
    try:
        s3Hook.load_string(rawData,key=newS3Key, bucket_name=s3BucketName) #push data to S3 bucket
        print(f"Raw data upload to s3 bucket {s3BucketName} successful")
    except Exception as e:
        print(f"Error on upload instance: {e}")
