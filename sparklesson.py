#SparkContext represents the connection to the Spark Cluster
from pyspark.sql import SparkSession
from pyspark import SparkContext as sc


# Verify SparkContext
print(sc)

# Print Spark version
print(sc.version)

# Import SparkSession from pyspark.sql
from pyspark.sql import SparkSession

# Create a SparkSession called spark
spark = SparkSession.builder.getOrCreate()

# Print spark
print(spark)


# Print the tables in the catalog
print(spark.catalog.listTables())

# Don't change this query
query = "FROM flights SELECT * LIMIT 10"

# Get the first 10 rows of flights
flights10 = spark.sql(query)

# Show the results
flights10.show()