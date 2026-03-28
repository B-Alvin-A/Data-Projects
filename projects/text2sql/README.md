# Text2SQL Analytics Project

## Overview
This project demonstrates the ability to translate business requirements into accurate, efficient SQL queries using a structured relational database.

It simulates a real-world analytics workflow where business questions are converted into SQL, validated for correctness, and optimized for performance.

---

## Key Features
- End-to-end SQL analytics workflow
- 25+ business-driven SQL queries
- Advanced SQL (CTEs, window functions, LAG, aggregations)
- Data validation and cross-checking layer
- Programmatic data generation using Python

---

## Tech Stack
- PostgreSQL
- Python (data generation)

---

## Database Schema

The project uses a normalized relational model for sales analytics.

### Tables
- **customers** — customer information and segmentation attributes  
- **products** — product catalog with categories  
- **orders** — transactional order data  
- **order_items** — line-level purchase details  

### Relationships
- One customer → many orders  
- One order → many order items  
- One product → many order items  

---

## Data Integrity

- Foreign key constraints enforce referential integrity  
- Cascading deletes prevent orphan records  
- CHECK constraints enforce valid values (price, quantity, status)  

### Constraint Verification
```sql
SELECT conname, contype FROM pg_constraint;