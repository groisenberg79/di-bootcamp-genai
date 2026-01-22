UPDATE film
SET language_id = 2
WHERE film_id = 1;

UPDATE film
SET language_id = 3
WHERE film_id = 2;

UPDATE film
SET language_id = 4
WHERE film_id = 3;

The FOREIGN KEY is address_id, and it references address_id in the table address. 
In order to use INSERT in customer, we need to specify the corresponding address_id in the
address table as one of the entries in VALUES (for each row). 

DROP TABLE customer_review;
This is an easy step, because this table is a child table to the new_film table

SELECT COUNT(*) AS not_returned FROM rental 
WHERE return_date IS NULL


SELECT title, rental_rate
FROM film
WHERE
	-- main query: select title, rental_rate for all film_id's in subquery 2 
	(film_id IN
		-- subquery 2: select all film_id's from inventory that are in subquery 1
		(SELECT film_id
		FROM inventory
		WHERE inventory_id IN
			-- subquery 1: select all rows in inventory not returned
			(SELECT inventory_id FROM rental WHERE return_date IS NULL)
		) 
	)
-- select only the 30 most expansive rates
ORDER BY rental_rate DESC LIMIT 30;

SELECT f.title, f.description
FROM film f
INNER JOIN film_actor fa 
	ON f.film_id = fa.film_id
INNER JOIN actor a 
	ON fa.actor_id = a.actor_id
WHERE 
	(f.description ILIKE '%sumo wrestler%') AND (a.first_name = 'Penelope') AND (a.last_name = 'Monroe');

SELECT f.title, f.length, f.rating, cat.name
FROM film f
INNER JOIN film_category fc
	ON f.film_id = fc.film_id
INNER JOIN category cat
	ON fc.category_id = cat.category_id
WHERE 
	f.length < 60 AND f.rating = 'R' AND cat.name = 'Documentary';

SELECT
  f.title,
  p.amount,
  r.return_date
FROM customer c
JOIN rental r    ON r.customer_id = c.customer_id
JOIN payment p   ON p.rental_id = r.rental_id
JOIN inventory i ON i.inventory_id = r.inventory_id
JOIN film f      ON f.film_id = i.film_id
WHERE c.first_name = 'Matthew'
  AND c.last_name  = 'Mahan'
  AND p.amount > 4.00
  AND r.return_date >= TIMESTAMP '2005-07-28'
  AND r.return_date <  TIMESTAMP '2005-08-01';

SELECT
	f.title,
	f.replacement_cost
FROM customer c
INNER JOIN rental r ON c.customer_id = r.customer_id
INNER JOIN inventory i ON r.inventory_id = i.inventory_id
INNER JOIN film f ON f.film_id = i.film_id
WHERE c.first_name = 'Matthew'
	AND c.last_name = 'Mahan'
	AND (f.title ILIKE '%boat%' OR f.description ILIKE '%boat%')
ORDER BY f.replacement_cost DESC
LIMIT 1;

	


