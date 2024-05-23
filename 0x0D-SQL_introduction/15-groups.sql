-- Get the count of all scores
SELECT UNIQUE score, COUNT(score) AS number FROM second_table ORDER BY number DESC;
