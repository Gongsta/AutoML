# Rename year column
planes = planes.withColumnRenamed("year", "plane_year")

# Join the DataFrames
model_data = flights.join(planes, on="tailnum", how="leftouter")

# Cast the columns from strings to integers
model_data = model_data.withColumn("arr_delay", model_data.arr_delay.cast("integer"))
model_data = model_data.withColumn("air_time",  model_data.air_time.cast("integer"))
model_data = model_data.withColumn("month",  model_data.month.cast("integer"))
model_data = model_data.withColumn("plane_year",  model_data.plane_year.cast("integer"))
