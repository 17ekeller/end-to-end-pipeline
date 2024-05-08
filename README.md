# Chicago Weather - Automated End to End Data Pipeline Project

## Introduction
This project aims to create a fully automated, end to end data pipeline using realtime, on the half-hour weather data from the City of Chicago. 

The data pipeline extracts, transforms and loads Chicago weather data into a datawarehouse at thirty minute time intervals and further produces visualization dashboards for analysis with a Busines Intelligence (BI) tool that is auto refreshed.

**Personal goals achieved on this project:**
 1. Upskilling Apache Spark and Airflow
 2. Utilzing AWS and S3 Abstraction
 3. Fully automating an end to end pipeline

## Architecture

### Data Source
The data is sourced from WeatherAPI.com's [Current Weather API](https://www.weatherapi.com/docs/). WeatherAPI.com is free and open source, all that is required is an API Key

### Business Logic
The data flow logic for this porject is: extract the weather data, load it to a data lake, clean and transform it and load it back into a processed data lake and then to a data warehouse. From there, utilizing a BI tool, the data is used for creating visulizations and dashboards for further analysis.

The raw data contains 33 datapoints about the weather, however only 14 were useful and therefore 19 points are dropped. Also, the data is retrieved in JSON format. The JSON file contains a double-nested object that needs to be flattened in order to properly write to the data warehouse.

### Data Destination
The data has four destinations along its journey through this pipeline. 

  1. "Raw Data" Amazon S3 Bucket
  2. "Processed Data" Amazon S3 Bucket
  3. MySQL Databse
  4. PowerBI Report Model

### Orchestration
Since there are multiple steps depending on one another, I chose to use Apache Airflow for this project, creating a Dag that runs at a time interval of 30 minutes.

## Tech Stack
  - Python
  -  Amazon S3 - data lake storag
  -  MySQL - data warehousing
  -  Apache Spark - cleaning, transforming and writing data
  -  Apache Airflow - workflow scheduling, batch processing, orchestration and S3 Abstraction
  -  Microsoft PowerBI - visualization

## Pipeline Architecture Visual
![Data pipeline flowchar](https://github.com/17ekeller/end-to-end-pipeline/blob/main/Pipeline%20Flowchart)


