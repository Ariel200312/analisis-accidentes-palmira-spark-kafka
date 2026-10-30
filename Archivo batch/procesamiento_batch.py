from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("AccidentesPalmira") \
    .getOrCreate()

df = spark.read.csv(
    "data/Accidentes_de_transito_Palmira.csv",
    header=True,
    inferSchema=True
)

df_limpio = df.dropDuplicates()

df_limpio.groupBy("DIA_SEMANA") \
    .count() \
    .show()

print("Total registros:", df_limpio.count())

spark.stop()
