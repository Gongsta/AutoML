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

