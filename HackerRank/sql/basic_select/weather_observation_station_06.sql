
-- Query the list of CITY names starting with vowels (i.e., a, e, i, o, or u) from STATION. Your result cannot contain duplicates.
-- https://www.hackerrank.com/challenges/weather-observation-station-6/problem

select DISTINCT city from STATION where city like 'a%' or city like 'e%'or city like 'i%'or city like 'o%'or city like 'u%';