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

### Step 4 — Staging Layer (Orders)

* Created staging table for orders (stg_orders)
* Applied data type casting for timestamp fields
* Implemented deduplication using ROW_NUMBER()
* Filtered out records with null primary identifiers
* Prepared clean and structured data for downstream modeling

### Step 5 — Staging Layer (Order Items)

* Created staging table for order items (stg_order_items)
* Defined composite key (order_id, order_item_id) for deduplication
* Converted price and freight_value to NUMERIC for financial accuracy
* Standardized shipping timestamp field
* Validated uniqueness and data integrity constraints

### Step 6 — Staging Layer (Customers)

* Created staging table for customers (stg_customers)
* Preserved both transactional (customer_id) and persistent (customer_unique_id) identifiers
* Implemented deduplication using customer_id
* Retained geographic fields without transformation for downstream modeling
* Identified customer uniqueness logic for future dimension table design

### Data Observation — Customer Identity Structure

* Identified that customer_unique_id represents the true customer entity
* Observed multiple customer_id values mapping to a single customer_unique_id
* Confirms that the dataset captures repeat purchases across different orders
* customer_id is treated as a transactional identifier, while customer_unique_id is used for dimensional modeling

### Step 7 — Staging Layer (Products)

* Created staging table for products (stg_products)
* Selected only analytically relevant fields to reduce noise
* Converted product dimensions and weight to numeric types
* Implemented deduplication using product_id
* Handled missing product categories by assigning 'unknown'
* Ensured data consistency for downstream dimensional modeling

### Step 8 — Staging Layer (Payments)

* Created staging table for payments (stg_payments)
* Preserved multiple payment records per order
* Applied composite deduplication using (order_id, payment_sequential)
* Converted payment fields to appropriate numeric types
* Prepared data for financial reconciliation and fact table integration
