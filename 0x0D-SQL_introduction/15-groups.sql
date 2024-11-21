-- lists the number of records with the same score in the table
-- the list should display the score and the number of records for the score
-- the list should be sorted by the number of records(descending)
SELECT score, COUNT(1) AS number FROM second_table GROUP BY score ORDER BY number DESC;
