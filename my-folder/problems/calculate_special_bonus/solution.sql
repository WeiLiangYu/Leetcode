# Write your MySQL query statement below
SELECT employee_id, 
    CASE
        WHEN mod(employee_id, 2) = 0 or name LIKE "M%" THEN 0
        ELSE salary
    END bonus
FROM Employees
ORDER BY employee_id;