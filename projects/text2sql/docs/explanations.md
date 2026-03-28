## Schema Design Rationale

The schema follows a normalized relational model:

- Separation of orders and order_items allows detailed transaction tracking
- Products are decoupled to enable category-based analytics
- Customers are linked to orders for behavioral analysis

This structure supports:
- Aggregations (revenue, counts)
- Trend analysis (time-based queries)
- Customer segmentation

## Constraint Design

The schema enforces referential integrity using explicit foreign key constraints:

- Orders must reference valid customers
- Order items must reference valid orders and products

Deletion rules:
- Customer deletion cascades to orders and order_items
- Products cannot be deleted if referenced in transactions

This ensures data consistency and prevents orphaned records.

## Data Population

Initial sample data was inserted to simulate a basic sales environment.

The dataset includes:
- Multiple customers and regions
- Products across categories
- Orders with varying statuses

This enables testing of joins, aggregations, and filtering logic.

## Data Generation Approach

Data was programmatically generated to ensure:

- Sufficient volume for meaningful analysis
- Distribution across time for trend analysis
- Variety in order statuses for filtering scenarios

This approach improves realism compared to static sample data.

## Validation Strategy

Validation queries were created to cross-check:

- Aggregated results vs base data
- Counts across different grouping levels
- Data integrity constraints

This ensures SQL outputs are reliable and accurate.