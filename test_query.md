# SQL Query Documentation: Active Users

## Query Name
`get_active_users_last_30_days`

## Purpose
Retrieves all active users who have logged in within the last 30 days.

## Test Query
```sql
SELECT 
    user_id,
    username,
    email,
    last_login_date
FROM 
    users
WHERE 
    status = 'active' 
    AND last_login_date >= DATE_SUB(CURRENT_DATE, INTERVAL 30 DAY)
ORDER BY 
    last_login_date DESC;