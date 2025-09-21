-- Query to find the names of employees who earn more than 2000 and have worked for less than 10 months, ordered by employee_id
-- https://www.hackerrank.com/challenges/salary-of-employees/problem
SELECT name
FROM Employee
WHERE salary > 2000
  AND months < 10
ORDER BY employee_id;