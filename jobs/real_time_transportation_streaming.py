from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from config import configuration
from spark_schema import *

def main():
    # Retrieve storage type from configuration or environment variable
    storage_type = configuration.get('STORAGE_TYPE', 'local_storage').lower()  # Default to 'local_storage' if not set

    # Set the output path based on storage type
    if storage_type == 's3':
        output_path = 's3a://spark-streaming-data-v1/data/'
        checkpoint_location = 's3a://spark-streaming-data-v1/checkpoints/'
    elif storage_type == 'local_storage':
        output_path = 'storage/data/'
        checkpoint_location = 'storage/checkpoints/'
    else:
        raise ValueError("Invalid storage type. Choose 'S3' or 'local_storage'.")

    # Initialize Spark session
    spark = SparkSession.builder.appName("realTimeTransportationStreaming")\
        .config("spark.jars.packages",
                "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0,"
                "org.apache.hadoop:hadoop-aws:3.3.1,"
                "com.amazonaws:aws-java-sdk:1.11.469")\
        .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")\
        .config("spark.hadoop.fs.s3a.access.key", configuration.get('AWS_ACCESS_KEY'))\
        .config("spark.hadoop.fs.s3a.secret.key", configuration.get('AWS_SECRET_KEY'))\
        .config("spark.hadoop.fs.s3a.aws.credentials.provider", "org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider")\
        .getOrCreate()
    
    # Adjust the log level to minimize the console output on executors
    spark.sparkContext.setLogLevel('WARN')

    def read_kafka_topic(topic, schema):
        return (spark.readStream
                .format('kafka')
                .option('kafka.bootstrap.servers', 'broker:29092')
                .option('subscribe', topic)
                .option('startingOffsets', 'earliest')
                .load()
                .selectExpr('CAST(value as STRING)')
                .select(from_json(col('value'), schema).alias('data'))
                .select('data.*')
                .withWatermark('timestamp', '2 minutes')
                )

    def streamWriter(input, checkpointFolder, output):
        return (input.writeStream
                .format('parquet')
                .option('checkpointLocation', checkpointFolder)
                .option('path', output)
                .outputMode('append')
                .start())

    # Reading data from Kafka topics
    vehicleDF = read_kafka_topic('vehicle_data', vehicleSchema).alias('vehicle')
    gpsDF = read_kafka_topic('gps_data', gpsSchema).alias('gps')
    trafficDF = read_kafka_topic('traffic_data', trafficSchema).alias('traffic')
    weatherDF = read_kafka_topic('weather_data', weatherSchema).alias('weather')
    emergencyDF = read_kafka_topic('emergency_data', emergencySchema).alias('emergency')

    # Writing the streams to the selected storage
    query1 = streamWriter(vehicleDF, checkpoint_location + 'vehicle_data', output_path + 'vehicle_data')
    query2 = streamWriter(gpsDF, checkpoint_location + 'gps_data', output_path + 'gps_data')
    query3 = streamWriter(trafficDF, checkpoint_location + 'traffic_data', output_path + 'traffic_data')
    query4 = streamWriter(weatherDF, checkpoint_location + 'weather_data', output_path + 'weather_data')
    query5 = streamWriter(emergencyDF, checkpoint_location + 'emergency_data', output_path + 'emergency_data')

    query5.awaitTermination()

if __name__ == "__main__":
    main()


#docker exec real_time_transportation_streaming-spark-master-1 spark-submit --master spark://spark-master:7077 --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0,org.apache.hadoop:hadoop-aws:3.3.1,com.amazonaws:aws-java-sdk:1.11.469 jobs/real_time_transportation_streaming.py