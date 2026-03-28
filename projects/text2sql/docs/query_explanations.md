### Query: Top 5 Customers by Revenue

**Business Question:**  
Who are the top 5 customers by total spending?

**Approach:**  
- Join customers → orders → order_items  
- Aggregate total spend  
- Sort descending  
- Limit to top 5