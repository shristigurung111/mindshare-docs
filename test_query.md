# SQL Query Explanation

This SQL query retrieves recent orders along with their customer details. The query selects the order ID, order date, total amount, order status, customer name, email, and phone number.

- **From**: The data is retrieved from the tables `orders` and `customers`.
- **Join condition**: The `customer_id` from the `orders` table must match the `customer_id` in the `customers` table.
- **Where conditions**:
  - Only orders from the last 7 days are selected (`o.order_date >= DATE_SUB(CURRENT_DATE, INTERVAL 7 DAY`).
  - Only orders with the status 'completed' or 'shipped' are included (`o.status IN ('completed', 'shipped')`).
- **Order by**: Orders are sorted by `order_date` in descending order.
- **Limit**: Only the top 50 results are returned.

This query provides a snapshot of recent orders along with customer details for further analysis or reporting.