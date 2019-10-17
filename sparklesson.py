#SparkContext represents the connection to the Spark Cluster
from pyspark.sql import SparkSession
from pyspark import SparkContext as sc
import pandas as pd


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

"""Getting from Spark Cluster to a Pandas Dataframe"""

# Don't change this query
query = "FROM flights SELECT * LIMIT 10"

#Flights would be a Spark Dataframe of flights
#This table contains a row for every flight that left Portland International Airport (PDX) 
#or Seattle-Tacoma International Airport (SEA) in 2014 and 2015.

#method takes a string containing the query and returns a Spark DataFrame with the results
flights = spark.sql(query)

# Show the results of the flights
flights.show()

# Convert the results to a pandas DataFrame
flights = flight_counts.toPandas()

# Print the head of pd_counts, i.e. the first 5 rows by default 
print(pd_counts.head())
#Prints the tail of pd_counts, i.e. the last 5 rows by default
print(pd_counts.tail())



"""Converting a Pandas Dataframe into a Spark Cluster"""
# Create pd_temp, a pandas 10x10 Dataframe 
pd_temp = pd.DataFrame(np.random.random(10))

# Create spark_temp from pd_temp. It transforms the pandas DataFrame into a Spark DataFrame and 
#is stored in spark_temp
spark_temp = spark.createDataFrame(pd_temp)

# Examine the tables in the catalog. At this point, spark_temp should not be in there
print(spark.catalog.listTables())

# Add spark_temp to the catalog, registered with the name "temp" 
#his safely creates a new temporary table if nothing was there before, or updates an existing table if one was already defined. 
#Use this method to avoid running into problems with duplicate tables, as opposed to .createTempView()
spark_temp.createOrReplaceTempView("temp")

# Examine the tables in the catalog again
print(spark.catalog.listTables())


"""Directly going from CSV to Spark Cluster"""
# Don't change this file path
file_path = "/usr/local/share/datasets/airports.csv"

# Read in the airports data
airports = spark.read.csv(file_path, header=True)

# Show the data
airports.show()








