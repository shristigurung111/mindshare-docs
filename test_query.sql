-- Test Query: Get active users from last 30 days
-- Test: Trigger workflow
SELECT 
    user_id,
    username,
    email,
    last_login_date, 
    created_date
FROM 
    users
WHERE 
    status = 'active' 
    AND last_login_date >= DATE_SUB(CURRENT_DATE, INTERVAL 30 DAY)
ORDER BY 
    created_date DESC;
