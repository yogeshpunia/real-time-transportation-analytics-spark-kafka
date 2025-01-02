from pyspark.sql.types import StructType, StructField, StringType, TimestampType, DoubleType, IntegerType

# vehicle_schema
vehicleSchema = StructType([
    StructField("id", StringType(), True),
    StructField("vehicleId", StringType(), True),
    StructField("timestamp", TimestampType(), True),
    StructField("location", StringType(), True),
    StructField("speed", DoubleType(), True),
    StructField("direction", StringType(), True),
    StructField("make", StringType(), True),
    StructField("model", StringType(), True),
    StructField("year", IntegerType(), True),
    StructField("fuel_type", StringType(), True)
])

# gps_schema
gpsSchema = StructType([
    StructField("id", StringType(), True),
    StructField("vehicleId", StringType(), True),
    StructField("timestamp", TimestampType(), True),
    StructField("speed", DoubleType(), True),
    StructField("direction", StringType(), True),
    StructField("vehicleType", StringType(), True)
])

# traffic_schema
trafficSchema = StructType([
    StructField("id", StringType(), True),
    StructField("vehicleId", StringType(), True),
    StructField("timestamp", TimestampType(), True),
    StructField("cameraId", StringType(), True),
    StructField("location", StringType(), True),
    StructField("snapshot", StringType(), True)
])

# weather_schema
weatherSchema = StructType([
    StructField("id", StringType(), True),
    StructField("vehicleId", StringType(), True),
    StructField("timestamp", TimestampType(), True),
    StructField("location", StringType(), True),
    StructField("temperature", DoubleType(), True),
    StructField("weatherCondition", StringType(), True),
    StructField("precipitation", DoubleType(), True),
    StructField("windSpeed", DoubleType(), True),
    StructField("humidity", IntegerType(), True),
    StructField("airQualityIndex", DoubleType(), True)
])

# emergency_schema
emergencySchema = StructType([
    StructField("id", StringType(), True),
    StructField("vehicleId", StringType(), True),
    StructField("timestamp", TimestampType(), True),
    StructField("location", StringType(), True),
    StructField("incidentId", StringType(), True),
    StructField("type", StringType(), True),
    StructField("status", StringType(), True),
    StructField("description", StringType(), True)
])
