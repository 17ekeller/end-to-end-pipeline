from airflow.providers.amazon.aws.hooks.s3 import S3Hook
import json

'''This script fetches the raw data, and transforms it by dropping unneeded data points and flattens the nested JSON data in the raw file. 
This prepares the data to be put into a Spark dataframe for push to MySql Database'''

def flattenData(d, parent_key='', sep='_') -> list:
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, dict):
            items.extend(flattenData(v, new_key, sep=sep))
        else:
            items.append((new_key, v))
    return items

def transformData() -> dict:

    s3Hook = S3Hook()

    bucketName = "chi-weather-raw"

    try:
        s3DataObjects = s3Hook.list_keys(bucket_name=bucketName) #fetch a list of filepaths from the S3 bucket

        sortedObjects = sorted(s3DataObjects, key=lambda key: s3Hook.get_key(bucket_name=bucketName, key=key).last_modified) #sorts list of objects in the bucket by the most recently modified timestamp

        lastModifiedKey = sortedObjects[-1] 
        fileContent = s3Hook.get_key(bucket_name=bucketName, key=lastModifiedKey).get()['Body'].read() #retrieves the most recently modified object from the bucket
        print("File fetched successfully")
    except Exception as e:
        print(f"Error obtaining most recent file: {e}")

    try:
        decodedData = fileContent.decode('utf-8')
        data = json.loads(decodedData)

        data = flattenData(data)
        print(type(data))
        toDel = [2,3,4,5,6,8,9,10,12,14,15,17,18,20,21,22,26,28,32] #list of datapoints to delete
        toDel.sort(reverse=True)
        for index in toDel: #filtering unneeded data
           del data[index]

        dataDict = {}
        for key, value in data:
            dataDict.setdefault(key, value) #write to dictionary in prep for processing to a Spark dataframe
        
        print("File processed successfully")

    except Exception as e:
        print(f"Error processing file: {e}")


    return(dataDict)
