SELECT genre FROM genres WHERE show_id IN(SELECT show_id FROM stars WHERE person_id IN(SELECT id FROM people WHERE name ="Robert Downey Jr."));

SELECT title FROM shows WHERE id IN(SELECT show_id FROM ratings ORDER BY rating DESC LIMIT 5);