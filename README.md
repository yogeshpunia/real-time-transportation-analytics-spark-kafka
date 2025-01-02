# Real-Time Transportation Data Streaming

This project demonstrates the ingestion and processing of real-time transportation data using Apache Kafka and Apache Spark. It simulates vehicle movement, generates real-time data streams for various types of transportation-related information, and processes this data using Spark Streaming for storage in S3 or local storage.

## Project Overview

This project provides a framework to simulate transportation data for vehicles, including GPS data, traffic camera snapshots, weather data, and emergency incidents. The data is sent to Apache Kafka topics, which are then consumed and processed by a Spark Streaming application. The processed data is stored in Parquet format either locally or in an AWS S3 bucket.

## Folder Structure
jobs/ ├── config.py # Configuration settings, including AWS credentials and storage options ├── real_time_transportation_streaming.py # Spark Streaming application for consuming and processing Kafka data ├── spark_schema.py # Defines the schema for each type of data (vehicle, GPS, traffic, weather, emergency) scripts/ ├── main.py # Data generator script that simulates transportation data and sends it to Kafka storage/ ├── data # Output folder for processed data ├── checkpoints # Checkpoint folder for Spark streaming jobs docker-compose.yml # Docker Compose configuration for Kafka and Spark services requirements.txt # List of dependencies required for the project system_architecture.png # Visual representation of the system architecture
