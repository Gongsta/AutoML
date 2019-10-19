# Rename year column
planes = planes.withColumnRenamed("year", "plane_year")

# Join the DataFrames
model_data = flights.join(planes, on="tailnum", how="leftouter")

# Cast the columns from strings to integers
model_data = model_data.withColumn("arr_delay", model_data.arr_delay.cast("integer"))
model_data = model_data.withColumn("air_time",  model_data.air_time.cast("integer"))
model_data = model_data.withColumn("month",  model_data.month.cast("integer"))
model_data = model_data.withColumn("plane_year",  model_data.plane_year.cast("integer"))

# Create the column plane_age, calculated by the substration of the plane manufacturing day (plane_year)
#to the current year (model_data.year)
model_data = model_data.withColumn("plane_age", model_data.year-model_data.plane_year)


# Create is_late 
model_data = model_data.withColumn("is_late", model_data.arr_delay > 0)



# Convert String values (in this case string of numbers like "52" to an integer)
model_data = model_data.withColumn("label", model_data.is_late.cast("integer"))

# Remove missing values
model_data = model_data.filter("arr_delay is not NULL and dep_delay is not NULL and air_time is not NULL and plane_year is not NULL")



#Transforming string to Integer (categorical data)
# Create a StringIndexer
carr_indexer = StringIndexer(inputCol="carrier", outputCol="carrier_index")

# Create a OneHotEncoder
carr_encoder = OneHotEncoder(inputCol="carrier_index", outputCol="carrier_fact")


# Create a StringIndexer
dest_indexer = StringIndexer(inputCol="dest", outputCol="dest_index")

# Create a OneHotEncoder
dest_encoder = OneHotEncoder(inputCol="dest_index", outputCol="dest_fact")


# Make a VectorAssembler
vec_assembler = VectorAssembler(inputCols=["month", "air_time", "carrier_fact", "dest_fact", "plane_age"], outputCol="features")