from airflow.providers.amazon.aws.hooks.s3 import S3Hook


def extractProcessedData() -> str:

    s3Hook = S3Hook()

    bucketName = "chi-processed-data"

    try:
        s3DataObjects = s3Hook.list_keys(bucket_name=bucketName)

        # Sorting objects by LastModified attribute
        sortedObjects = sorted(s3DataObjects, key=lambda key: s3Hook.get_key(bucket_name=bucketName, key=key).last_modified) #sorts list of objects in the bucket by the most recently modified timestamp
        lastModifiedKey = sortedObjects[-1]
        fileContent = s3Hook.get_key(bucket_name=bucketName, key=lastModifiedKey).get()['Body'].read() #retrieves the most recently modified object from the bucket
        print("Processed file fetched successfully")

    except Exception as e:
        print("Error fetching processed file {e}")
    return fileContent