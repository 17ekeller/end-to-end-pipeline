from airflow.providers.amazon.aws.hooks.s3 import S3Hook
from pyspark.sql import SparkSession
from pyspark.sql import DataFrame
from processedSchema import schema
from extractProcessedData import extractProcessedData
from datetime import datetime
import json


def dictionaryTransform(dataDict) -> dict:

    try:
        if 'localtime' in dataDict:
            value = dataDict['localtime']
            # Delete the old key
            del dataDict['localtime']
            # Add a new key with the updated name and the original value
            dataDict['local_time'] = value
            print("Localtime name changed successfully")
    except Exception as e:
        print(f"Error on changing localtime name: {e}")

    try:
        datetime_str = dataDict.get('local_time', None)
        if datetime_str:
            timestamp = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M')
            dataDict['local_time'] = timestamp
        print("Dictionary transform successful")
    except Exception as e:
        print(f"Dictionary transform error: {e}")


    return dataDict


def dataToDataFrame(decodedData) -> DataFrame:
    spark = SparkSession.builder \
        .appName("Dataframe Creator") \
        .getOrCreate()

    try:
        processedDF = spark.createDataFrame([decodedData], schema=schema)
        print("Dataframe created Successfully")
    except Exception as e:
        print(f"Dataframe creation error: {e}")

    return processedDF



def main() -> DataFrame:

    fileContent = extractProcessedData()
    decodedData = fileContent.decode('utf-8')
    dataDict = json.loads(decodedData)
    transformedData = dictionaryTransform(dataDict)
    dfData = dataToDataFrame(transformedData)
    return dfData