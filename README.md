# :partly_sunny: Chicago Weather - Automated End to End Data Pipeline Project :cloud_with_lightning:

## :white_check_mark:Introduction
This project aims to create a fully automated, end to end data pipeline using realtime, on the half-hour weather data from the City of Chicago via [Current Weather API](https://www.weatherapi.com/docs/). 

Using modern tech stack tools, the data pipeline orchestrates the extraction, transformation, and loading of Chicago weather data into a data warehouse every thirty minutes. Additionally, it seamlessly generates auto-refreshed visualization dashboards using a direct connection to PowerBI for insightful analysis.

***Personal goals achieved on this project:***
 1. Upskilling Apache Spark and Airflow
 2. Utilzing AWS and S3 Abstraction
 3. Fully automating an end-to-end data pipeline including visual dashboards

## :triangular_ruler:  Architecture

### Data Source
The data is sourced from WeatherAPI.com's [Current Weather API](https://www.weatherapi.com/docs/). WeatherAPI.com is free and open source, all that is required is an API Key

### Business Logic
The data pipeline for this project follows a systematic flow to ensure the accuracy, cleanliness, and accessibility of the Chicago weather data. Here's a breakdown of the business logic:

- ***Data Extraction:*** Weather data is sourced in real-time from WeatherAPI.com's Current Weather API. The data includes a variety of parameters related to Chicago's current weather conditions.
- ***Data Lake Storage:*** The raw weather data is stored in an Amazon S3 bucket. Storing the data in its raw format allows for easy access and scalability, provides transparency and ease of access to original data sets.
- ***Data Transformation and Cleaning:*** The raw data contains 33 data points, but only 14 are useful for analysis. Therefore, a transformation process is initiated to filter out the irrelevant data points and clean the dataset. Additionally, the double nested JSON format of the data is flattened to ensure compatibility with downstream processes. Also defined is the data schema, used for loading the proper datatypes into a pySpark dataframe.
- ***Processed Data Storage:*** The cleaned and transformed data is then stored in another Amazon S3 bucket named "Processed Data." This serves as a repository for the refined data, making it readily available for further analysis.
- ***Data Warehousing:*** The processed data is loaded into a MySQL database, serving as the data warehouse. This structured storage allows for efficient querying and retrieval of historical weather data.
- ***Visualization and Analysis:*** Utilizing a Business Intelligence (BI) tool, in this case, Microsoft PowerBI, visualization dashboards are created utilizing a direct link to the MySQL database and Power Query. These dashboards are auto refreshed and provide insights into Chicago's weather trends, patterns, and anomalies, aiding stakeholders in making informed decisions.

The data pipeline boasts complete automation from start to finish, eliminating manual intervention and streamlining the entire process. This automation enhances efficiency by executing tasks at scheduled intervals without human intervention, ensuring consistent and reliable data processing.

### Data Destination
The data has four destinations along its journey through this pipeline. 

  1. "Raw Data" Amazon S3 Bucket
  2. "Processed Data" Amazon S3 Bucket
  3. MySQL Databse
  4. PowerBI Report Model

### Orchestration
Since there are multiple steps depending on one another, I chose to use Apache Airflow for this project, creating a DAG that runs at a time interval of 30 minutes.

Airflow is also utilized for an abstraction layer with S3 Hooks from the airflow.providers.amazon.aws.hooks module in Python.

## :books:Tech Stack
  -  Python
  -  Amazon S3 - data lake storage
  -  MySQL - data warehousing
  -  Apache Spark - cleaning, transforming and writing data
  -  Apache Airflow - workflow scheduling, batch processing, orchestration and S3 Abstraction
  -  Microsoft PowerBI - visualization

## Pipeline Architecture Visual
![Data pipeline flowchar](https://github.com/17ekeller/weather-endtoend-pipeline/blob/main/Data%20Flow%20Visual)

## DAG Graph Visual
![Dag Flow](https://github.com/17ekeller/end-to-end-pipeline/blob/main/Dagflow)

## Power BI Dashboard
![PBI Dashboard](https://github.com/17ekeller/weather-endtoend-pipeline/blob/main/PBI%20Dashboard)

## Contact
:handshake: Connect with me [LinkedIn](https://www.linkedin.com/in/eric-keller-binf-b7303418b/)

## Acknowledgements
- [Data Engineering Wiki](https://dataengineering.wiki/Index)
- [Apache Airflow Docs](https://airflow.apache.org/docs/)
- [Apache Spark Docs](https://spark.apache.org/docs/latest/)
- [Apache PySpark Docs](https://spark.apache.org/docs/latest/api/python/index.html)
- [Amazon S3 Docs](https://docs.aws.amazon.com/s3/)
- [Useful IBM Data Topics](https://www.ibm.com/topics/data-warehouse)

