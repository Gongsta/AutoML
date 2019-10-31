import pyspark

#View pyspark version
print(pyspark.__version__)


from pyspark.sql import SparkSession
from pyspark import SparkContext

sc = SparkContext(appName='MyApp')

#local[*] specifies the use of all cores available on the local machine
spark = SparkSession.builder.master('local[*]')
spark = SparkSession.builder.appName('first_spark_application')
spark = SparkSession.builder.getOrCreate()

# Print the version of SparkContext
print("The version of Spark Context in the PySpark shell is", sc.version)

# Print the Python version of SparkContext
print("The Python version of Spark Context in the PySpark shell is", sc.pythonVer)

# Print the master of SparkContext
print("The master of Spark Context in the PySpark shell is", sc.master)


#Using lambda() and map() functions
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Print my_list in the console
print("Input list is", my_list)

# Square all numbers in my_list
squared_list_lambda = list(map(lambda x: x **2, my_list))

# Print the result of the map function
print("The squared numbers are", squared_list_lambda)

#Filter() function
# Print my_list2 in the console
my_list2 = [10, 21, 31, 40, 51, 60, 72, 80, 93, 101]
print("Input list is:", my_list2)

# Filter numbers divisible by 10
filtered_list = list(filter(lambda x: (x%10 == 0), my_list2))

# Print the numbers divisible by 10
print("Numbers divisible by 10 are:", filtered_list)

#LEARNING ABOUT RDD!
# Create an RDD from a list of words
RDD = sc.parallelize(["Spark", "is", "a", "framework", "for", "Big Data processing"])

# Print out the type of the created object
print("The type of RDD is", type(RDD))

# Print the file_path
print("The file_path is", file_path)

# Create a fileRDD from file_path, but with the method textFile because it takes the filepath instead of the direct data
fileRDD = sc.textFile(file_path)

# Check the type of fileRDD
print("The file type of fileRDD is", type(fileRDD))


# Check the number of partitions in fileRDD
print("Number of partitions in fileRDD is", fileRDD.getNumPartitions())

# Create a fileRDD_part from file_path with 5 partitions
fileRDD_part = sc.textFile(file_path, minPartitions = 5)

# Check the number of partitions in fileRDD_part
print("Number of partitions in fileRDD_part is", fileRDD_part.getNumPartitions())


# Create map() transformation to cube numbers
cubedRDD = numbRDD.map(lambda x: x**3)

# Collect the results
numbers_all = cubedRDD.collect()

# Print the numbers from numbers_all
for numb in numbers_all:
	print(numb)

