## Database Schema

This project uses a relational data model designed for sales analytics.

### Tables
- customers: stores customer information
- products: stores product catalog
- orders: stores customer orders
- order_items: stores line-level transaction data

### Relationships
- One customer can have many orders
- One order can have many order items
- Each order item is linked to one product

### Data Integrity Constraints

- Foreign key constraints enforce relationships between tables
- Cascading deletes ensure no orphan records
- CHECK constraints enforce valid numeric and status values

### Constraint Verification

Constraints were verified using PostgreSQL system catalog:

```sql
SELECT conname, contype FROM pg_constraint;

## Sample Data

The database includes sample transactional data for:

- Customers across multiple regions
- Product catalog with categories
- Orders with different statuses
- Order items representing purchases

This dataset supports analytical queries such as:
- Revenue analysis
- Customer behavior tracking
- Product performance

## Data Generation

Sample data is generated using a Python script to simulate a realistic sales environment.

Dataset size:
- ~200 customers
- ~300 orders
- ~900 order items

The generator introduces:
- Multiple regions
- Varied order dates
- Different order statuses (completed, pending, cancelled)

This enables realistic analytical querying and testing.

## Data Validation

Validation queries were implemented to ensure:

- Revenue consistency across aggregations
- No orphan or invalid records
- No negative transaction values
- Logical consistency in reporting queries

# 🗂 Project Structure
text2sql/
├── schema/
│   ├── schema.sql
├── data/
│   ├── sample-data.sql(myfile used)
│   └── generator.py
├── queries/
├── validation/
|   ├── validation_checks.sql
├── docs/
│   ├── ERD.png
│   ├── explanations.md
│   └── query_explanations.md
└── README.md