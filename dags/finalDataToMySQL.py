from pyspark.sql import SparkSession
from transformProcessedData import main
from config import username, passkey

'''This script takes the processed data file from S3 and utilizing apache Spark,
puts the processed data into a dataframe, connects to a MySQL database and appends the newly extracted and transformed 
data into the database for further querying and visualizations'''

def toMySQL() -> None:
    
    driver_class = "com.mysql.cj.jdbc.Driver"
    
    #initialize a spark session
    #.config - Configures Spark to use the MySQL JDBC driver. This ensures that the driver is available on the Spark driver's classpath.
    spark = SparkSession.builder \
        .appName("Write to MySQL") \
        .config("spark.driver.extraClassPath", "/Users/erickeller/Desktop/Spark/spark-3.5.1-bin-hadoop3/jars/mysql-connector-j-8.4.0.jar") \
        .getOrCreate()

    host = "localhost"
    port = "3306"
    database = "ChicagoWeather"
    user = username
    password = passkey

    jdbc_url = f"jdbc:mysql://{host}:{port}/{database}" #Constructs the JDBC URL for connecting to the MySQL database.

    properties = { 
        "user": user,
        "password": password,
        "driver": driver_class
    }

    # Write data to MySQL
    try:
        data.write \
            .format("jdbc") \
            .option("url", jdbc_url) \
            .option("dbtable", "Weather_Data") \
            .option("user", user) \
            .option("password", password) \
            .option("driver", driver_class) \
            .mode("append")\
            .jdbc(jdbc_url, "Weather_Data", properties=properties)
        print("Data upload to MySQL successful")
    except Exception as e:
        print(f"Error: {e}")


    spark.stop()

if __name__ == "__main__":
    data = main()
    data.show()
    toMySQL()