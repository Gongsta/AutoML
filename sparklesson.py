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


#attribute called catalog lists all the data inside the cluster. 
#This attribute has a few methods for extracting different pieces of information.
print(spark.catalog.listTables())

"""Getting from Spark Cluster to a Pandas Dataframe"""

# Don't change this query. The query says to select all items with limit 10 from the flights table
query = "FROM flights SELECT * LIMIT 10"

#flights would be a Spark Dataframe of flights
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


"""Manipulation Data"""

# Create the DataFrame flights
flights = spark.table("flights")

# Show the head
flights.show()

#Modify the Dataframe in order to add a new column called duration_hrs with flight times in hours.  
#Note that Spark Dataframes are immutable, so columns can't be updated in place
flights = flights.withColumn("duration_hrs", flights.air_time/60)


#FOR ROWS
# Filter flights by passing a string. This returns a Spark Dataframe of all flights with a distance greater than 1000
long_flights1 = flights.filter("distance > 1000")

# Filter flights by passing a column of boolean values
long_flights2 = flights.filter(flights.distance > 1000)

# Print the data to check they're equal
long_flights1.show()
long_flights2.show()



#FOR COLUMNS
#Selecting only a set of columns and filtering them
#.select() returns the columns selected.
#.withColumn() returns all the columns of the DataFrame in addition to the one you defined. 
selected1 = flights.select("tailnum", "origin", "dest")

# Select the second set of columns
temp = flights.select(flights.origin, flights.dest, flights.carrier)

#Notice that temp and selected1 are the same thing
#These arguments can either be the column name as a string (one for each column) 
#or a column object (using the df.colName syntax)


# Define first filter
filterA = flights.origin == "SEA"

# Define second filter
filterB = flights.dest == "PDX"

# Filter the data, first by filterA then by filterB
selected2 = temp.filter(filterA).filter(filterB)


#you can perform any column operation and the .select() method will return the transformed column


# Define avg_speed
#.alias() renames a column selected
avg_speed = (flights.distance/(flights.air_time/60)).alias("avg_speed")

# Select the correct columns
speed1 = flights.select("origin", "dest", "tailnum", avg_speed)

# Create the same table using a SQL expression
speed2 = flights.selectExpr("origin", "dest", "tailnum", "distance/(air_time/60) as avg_speed")


# Find the shortest flight from PDX in terms of distance
flights.filter(flights.origin == "PDX").groupBy().min("distance").show()

# Find the longest flight from SEA in terms of air time
flights.filter(flights.origin == "SEA").groupBy().max("air_time").show()


# Average duration of Delta flights
flights.filter(flights.origin == "SEA").filter(flights.carrier == "DL").groupBy().avg("air_time").show()

# Total hours in the air
flights.withColumn("duration_hrs", flights.air_time/60).groupBy().sum("duration_hrs").show()




#Grouping
# Group by tailnum
by_plane = flights.groupBy("tailnum")

# Number of flights each plane made
by_plane.count().show()

# Group by origin
by_origin = flights.groupBy("origin")

# Average duration of flights from PDX and SEA
by_origin.avg("air_time").show()


# Import pyspark.sql.functions as F
import pyspark.sql.functions as F

# Group by month and dest
by_month_dest = flights.groupBy("month", "dest")

# Average departure delay by month and destination
by_month_dest.avg("dep_delay").show()

# Standard deviation of departure delay
by_month_dest.agg(F.stddev("dep_delay")).show()



# Examine the data
airports.show()
# Rename the faa column
airports = airports.withColumnRenamed("faa", "dest")

# Join the DataFrames
flights_with_airports = flights.join(airports, "dest", how="leftouter")

# Examine the new DataFrame
flights_with_airports.show()













