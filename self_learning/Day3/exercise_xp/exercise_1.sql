-- SELECT name FROM language;

-- SELECT 
-- 	f.title, 
-- 	f.description,
-- 	l.name
-- FROM film f
-- INNER JOIN language l
-- ON f.language_id = l.language_id;

-- SELECT 
-- 	f.title, 
-- 	f.description,
-- 	l.name
-- FROM language l
-- LEFT JOIN film f
-- ON f.language_id = l.language_id
-- ORDER BY l.name;

-- CREATE TABLE new_film (
-- 	id SERIAL PRIMARY KEY,
-- 	name TEXT NOT NULL
-- );

-- INSERT INTO new_film (name)
-- VALUES
-- 	('The Amazing Movie'),
-- 	('Dancing With the Wolves'),
-- 	('A Crypto Love Affair'),
-- 	('The Big Hole');

-- CREATE TABLE customer_review (
-- 	review_id SERIAL PRIMARY KEY,
-- 	film_id INTEGER NOT NULL,
-- 	language_id INTEGER NOT NULL,
-- 	title VARCHAR(100) NOT NULL,
-- 	score INTEGER NOT NULL,
-- 	review_text TEXT NOT NULL,
-- 	last_update DATE NOT NULL,

-- 	CONSTRAINT customer_review_film_id_fkey
-- 		FOREIGN KEY (film_id) REFERENCES new_film(id)
-- 		ON DELETE CASCADE,

-- 	CONSTRAINT score_valid_range_chk
-- 		CHECK (score BETWEEN 1 AND 10)
-- );
