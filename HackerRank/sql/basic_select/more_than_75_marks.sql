-- query to select names of students with marks greater than 75, ordered by the last three characters of their names and then by their IDs.
-- https://www.hackerrank.com/challenges/more-than-75-marks/problem
SELECT Name
FROM STUDENTS
WHERE Marks > 75
ORDER BY RIGHT(Name, 3),
  ID;