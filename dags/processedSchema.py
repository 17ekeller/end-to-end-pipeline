from pyspark.sql.types import StructType, StructField, DoubleType, StringType, IntegerType, TimestampType

#defining the schema for creating pyspark dataframe
schema = StructType([
    StructField("name", StringType(), True),
    StructField("region", StringType(), True),
    StructField("temp_f", DoubleType(), True),
    StructField("condition_text", StringType(), True),
    StructField("wind_mph", DoubleType(), True),
    StructField("wind_dir", StringType(), True),
    StructField("precip_in", DoubleType(), True),
    StructField("humidity", IntegerType(), True),
    StructField("cloud", IntegerType(), True),
    StructField("feelslike_f", DoubleType(), True),
    StructField("vis_miles",DoubleType(), True),
    StructField("uv", DoubleType(), True),
    StructField("gust_mph", DoubleType(), True),
    StructField("local_time", TimestampType(), True)
])
