-- SELECT name FROM language;

-- SELECT 
-- 	film.title, 
-- 	film.description,
-- 	language.name
-- FROM film
-- INNER JOIN language
-- ON film.language_id = language.language_id;

-- SELECT 
-- 	film.title, 
-- 	film.description,
-- 	language.name
-- FROM language
-- LEFT JOIN film
-- ON film.language_id = language.language_id
-- ORDER BY language.name;

-- CREATE TABLE new_film (
-- 	id SERIAL PRIMARY KEY,
-- 	name TEXT NOT NULL
-- );
