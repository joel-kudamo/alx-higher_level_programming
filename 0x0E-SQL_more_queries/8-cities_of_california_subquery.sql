-- lists all the cities of California that can be found in the database
-- results sorted in ascending order by cities
SELECT id, name FROM cities WHERE state_id IN (SELECT id FROM states WHERE name = "California") ORDER BY id;
