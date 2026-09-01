-- Get recent orders with customer details
SELECT 
    o.order_id,
    o.order_date,
    o.total_amount,
    o.status,
    c.customer_name,
    c.email,
    c.phone
FROM 
    orders o
JOIN 
    customers c ON o.customer_id = c.customer_id
WHERE 
    o.order_date >= DATE_SUB(CURRENT_DATE, INTERVAL 7 DAY)
    AND o.status IN ('completed', 'shipped')
ORDER BY 
    o.order_date DESC
LIMIT 50;
