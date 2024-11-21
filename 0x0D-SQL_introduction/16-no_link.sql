-- lists all records of the table in MySQL server
-- rows without a name value are not listed
-- results should display the score and the name in that order
-- records should be listed by descending score
SELECT score, name FROM second_table HAVING name IS NOT NULL ORDER BY score DESC;
