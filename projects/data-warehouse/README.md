# Data Warehouse + ETL Pipeline (E-Commerce)

## Project Overview

This project demonstrates the design and implementation of a modern data warehouse using PostgreSQL. It simulates a real-world ETL pipeline by transforming raw transactional e-commerce data into a structured star schema for analytics.

## Objectives

* Design a scalable data model (star schema)
* Build a multi-layer ETL pipeline (Raw → Staging → Warehouse)
* Perform data cleaning and transformation using SQL
* Generate business insights through analytical queries
* Implement data quality validation checks

## Dataset

This project uses the Brazilian E-Commerce Public Dataset (Olist) from Kaggle, which contains real-world transactional data including orders, customers, products, and payments.

## Architecture

The project follows a 3-layer architecture:

* **Raw Layer**: Stores ingested data in its original format
* **Staging Layer**: Cleans and standardizes data
* **Warehouse Layer**: Contains fact and dimension tables (star schema)

## Tech Stack

* PostgreSQL
* SQL

## Project Structure
data-warehouse-project/
│
├── data/
│   └── raw/                  # CSV files
│
├── sql/
│   ├── 01_raw/
│   ├── 02_staging/
│   ├── 03_warehouse/
│   ├── 04_analytics/
│   └── 05_quality_checks/
│
├── diagrams/
│   └── star_schema.png
│
├── README.md

## Progress Log

### Step 1 — Project Setup

* Selected domain: E-commerce
* Selected dataset: Olist Kaggle dataset
* Defined project objectives and architecture

### Step 2 — Raw Layer Design

* Identified required source tables from dataset
* Designed raw layer schema using a schema-on-read approach
* All fields stored as TEXT to preserve source integrity
* Added ingestion timestamp (ingested_at) for auditability
* No constraints applied to allow raw data flexibility

### Step 3 — Data Ingestion (Raw Layer)

* Loaded CSV data into PostgreSQL raw tables using COPY command
* Configured Docker volume mapping for file accessibility
* Successfully ingested transactional, customer, product, and payment data
* Performed initial row count validation to confirm successful load
