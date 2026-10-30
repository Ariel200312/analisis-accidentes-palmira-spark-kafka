from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("KafkaStreaming") \
    .getOrCreate()

stream = spark.readStream \
    .format("kafka") \
    .option(
        "kafka.bootstrap.servers",
        "localhost:9092"
    ) \
    .option(
        "subscribe",
        "accidentes"
    ) \
    .load()

datos = stream.selectExpr(
    "CAST(value AS STRING) AS dia"
)

query = datos.writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

query.awaitTermination()
