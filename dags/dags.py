from datetime import timedelta, datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
import logging

import os

os.environ['NO_PROXY'] = '*'

from rawDataToS3 import uploadRawData
from processedDataToS3 import uploadProcessedData

#functions for tasks
def raw_data_task():
    try:
        uploadRawData()
    except Exception as e:
        logging.exception("Error occurred in raw_data_task: %s", str(e))
        raise

def transform_data_task():
    try:
        uploadProcessedData()
    except Exception as e:
        logging.exception("Error occurred in transform_data_task: %s", str(e))
        raise

#function for spark submit task
def spark_submit_task():
    spark_command = "spark-submit --jars /Users/erickeller/Desktop/Spark/spark-3.5.1-bin-hadoop3/jars/mysql-connector-j-8.4.0.jar /Users/erickeller/airflow/dags/finalDataToMySQL.py"
 
    return spark_command

#DAG arguments
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,
    'retry_delay': timedelta(minutes=1),
    'start_date': datetime(2024, 5, 8),
    'catchup': False
}

#Instantiate DAG
dag = DAG(
    'chiWeatherPipeline',
    default_args=default_args,
    description='Dag for the Chicago Weather Data Pipeline',
    schedule_interval=timedelta(minutes=30),
)

# Define tasks
raw_data_operator = PythonOperator(
    task_id='raw_data_task',
    python_callable=raw_data_task,
    dag=dag,
)

transform_data_operator = PythonOperator(
    task_id='transform_data_task',
    python_callable=transform_data_task,
    dag=dag,
)

spark_submit_operator = BashOperator(
    task_id='spark_submit_task',
    bash_command=spark_submit_task(),
    dag=dag,
)

#task dependencies
raw_data_operator >> transform_data_operator >> spark_submit_operator
