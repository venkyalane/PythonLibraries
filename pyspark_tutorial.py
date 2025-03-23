from pyspark.sql import SparkSession

SparkSession.builder.master("local[*]").getOrCreate().stop()

spark = SparkSession.builder.remote("sc://localhost:15002").getOrCreate()