-- lists alll cities contained in the database
SELECT c.id, c.name, s.name FROM cities AS c INNER JOIN states AS s ON c.stat_id = s.id ORDER BY c.id;
