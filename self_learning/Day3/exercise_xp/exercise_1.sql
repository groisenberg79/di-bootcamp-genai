SELECT name FROM language;

SELECT 
	f.title, 
	f.description,
	l.name
FROM film f
INNER JOIN language l
ON f.language_id = l.language_id;

SELECT 
	f.title, 
	f.description,
	l.name
FROM language l
LEFT JOIN film f
ON f.language_id = l.language_id
ORDER BY l.name;

CREATE TABLE new_film (
	id SERIAL PRIMARY KEY,
	name TEXT NOT NULL
);

INSERT INTO new_film (name)
VALUES
	('The Amazing Movie'),
	('Dancing With the Wolves'),
	('A Crypto Love Affair'),
	('The Big Hole');

CREATE TABLE customer_review (
	review_id SERIAL PRIMARY KEY,
	film_id INTEGER NOT NULL,
	language_id INTEGER NOT NULL,
	title VARCHAR(100) NOT NULL,
	score INTEGER NOT NULL,
	review_text TEXT NOT NULL,
	last_update DATE NOT NULL DEFAULT CURRENT_DATE,

	CONSTRAINT customer_review_film_id_fkey
		FOREIGN KEY (film_id) REFERENCES new_film(id)
		ON DELETE CASCADE,

	CONSTRAINT score_valid_range_chk
		CHECK (score BETWEEN 1 AND 10)
);

INSERT INTO customer_review(film_id, language_id, title, score, review_text)
VALUES
	(1, 1, 'Cool Movie!', 10, 'Lives up to its title -- truly amazing! Everything is amazing in this movie! Wow!'),
	(2, 1, 'Excellent, with a caveat', 9, 'I loved this movie, but my only complain is that there were too many wolves. Sometimes less is more.');

-- This shows two movie reviews
SELECT * FROM customer_review;

DELETE FROM new_film WHERE name = 'The Amazing Movie';

-- Now this SELECT statement will only show 1 movie review, 
-- because of the ON DELETE CASCADE constraint.
SELECT * FROM customer_review