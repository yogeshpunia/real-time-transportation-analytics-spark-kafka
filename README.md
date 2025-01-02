
# Real-Time Transportation Streaming with Apache Kafka & Spark

## Project Overview

This project demonstrates a real-time data streaming pipeline using Apache Kafka, Apache Spark, and Docker. It simulates transportation-related data (vehicle, GPS, traffic, weather, and emergency incidents) and processes it using Spark Streaming. The processed data is then stored either locally or in AWS S3.

## Features

- Simulated real-time transportation data generation (vehicle, GPS, traffic, weather, and emergency data).
- Data produced to Kafka topics in real-time.
- Data processing using Spark Streaming.
- Storage of processed data in Parquet format.
- Option to store processed data in local storage or AWS S3.

## Project Structure

```
jobs/
│
├── config.py                   # Configuration file for AWS and storage settings
├── real_time_transportation_streaming.py  # Main Spark Streaming job
├── spark_schema.py              # Schema definitions for the different data types (vehicle, gps, etc.)
│
scripts/
│
├── main.py                      # Python script for simulating and producing data to Kafka
│
storage/
│
├── data/                        # Directory for storing processed data
├── checkpoints/                 # Directory for storing Spark checkpoints
│
docker-compose.yml               # Docker Compose configuration file for setting up Kafka and Spark
requirements.txt                # Python dependencies for the project
system_architecture.png         # Diagram of the system architecture
```

## Setup and Run

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/real-time-transportation-streaming.git
cd real-time-transportation-streaming
```

### 2. Install Dependencies

Install the necessary Python dependencies using `pip`:

```bash
pip install -r requirements.txt
```

Make sure you have Docker and Docker Compose installed on your machine for setting up Kafka and Spark containers.

### 3. Set Up Kafka and Spark Using Docker

The project uses Docker Compose to set up Kafka and Spark. To start the services, run:

```bash
docker-compose up -d
```

This will start the Kafka broker and Spark services in detached mode. You can verify that the containers are running using:

```bash
docker-compose ps
```

Ensure that the following services are up and running:
- **Kafka**: The Kafka broker that will be used for message streaming.
- **Zookeeper**: The Zookeeper service used by Kafka.
- **Spark Master & Worker**: The Spark cluster services for running Spark jobs.

### 4. Configure AWS (Optional)

If you plan to use AWS S3 for storing processed data, you need to provide your AWS credentials. Update the `jobs/config.py` file with your AWS credentials:

```python
configuration = {
    "AWS_ACCESS_KEY": "your-aws-access-key",
    "AWS_SECRET_KEY": "your-aws-secret-key",
    "STORAGE_TYPE": "s3"  # Set to "local_storage" for local storage
}
```

If you prefer to store the processed data locally, set the `"STORAGE_TYPE"` to `"local_storage"`.

### 5. Generate and Produce Data to Kafka

Run the `scripts/main.py` script to simulate and produce transportation data (vehicle, GPS, traffic, weather, and emergency) to Kafka topics:

```bash
python scripts/main.py
```

This script will continuously generate and send random data to Kafka topics: `vehicle_data`, `gps_data`, `traffic_data`, `weather_data`, and `emergency_data`.

### 6. Start Spark Streaming Job

Run the Spark streaming job to process data from the Kafka topics and write the results to the storage location:

```bash
docker exec real_time_transportation_streaming-spark-master-1 spark-submit --master spark://spark-master:7077 --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0,org.apache.hadoop:hadoop-aws:3.3.1,com.amazonaws:aws-java-sdk:1.11.469 jobs/real_time_transportation_streaming.py
```

This command will start the Spark job that consumes the data from Kafka, processes it using Spark Streaming, and writes it to the storage location (either local or S3).

### 7. Monitor the Output

You can monitor the processed data in the following locations:

- **Local Storage**: The processed data will be saved in the `storage/data/` directory.
- **AWS S3**: If using AWS S3, the data will be stored in the specified S3 bucket.

The data will be saved in Parquet format.

### 8. Stopping the Services

To stop the Docker containers (Kafka and Spark), run:

```bash
docker-compose down
```

This will stop and remove the containers from your system.

## Conclusion

Once the setup and run steps are completed, you will have a working system that simulates vehicle data, streams it to Kafka, processes it in real-time with Apache Spark, and stores the results for later use.
