-- SELECT * FROM customer

-- SELECT first_name || ' ' || last_name AS full_name FROM customer

-- SELECT DISTINCT create_date FROM customer

-- SELECT * FROM customer ORDER BY first_name

-- SELECT 
-- 	film_id,
-- 	title,
-- 	description,
-- 	release_year,
-- 	rental_rate
-- FROM
-- 	film
-- ORDER BY
-- 	rental_rate

-- SELECT address, phone FROM address WHERE district = 'Texas'	

-- SELECT * FROM film WHERE film_id IN (15, 150)

-- SELECT
-- 	film_id,
-- 	title,
-- 	description,
-- 	length,
-- 	rental_rate
-- FROM
-- 	film
-- WHERE
-- 	title = 'The Dark Knight'

-- SELECT
-- 	film_id,
-- 	title,
-- 	description,
-- 	length,
-- 	rental_rate
-- FROM
-- 	film
-- WHERE
-- 	title LIKE 'Th%'

-- SELECT * FROM film ORDER BY rental_rate ASC LIMIT 10

-- SELECT *
-- FROM film
-- ORDER BY rental_rate ASC
-- OFFSET 10
-- LIMIT 10;

-- SELECT 
-- 	customer.first_name, 
-- 	customer.last_name, 
-- 	payment.amount, 
-- 	payment.payment_date
-- FROM 
-- 	customer
-- INNER JOIN 
-- 	payment
-- ON 
-- 	customer.customer_id = payment.customer_id
-- ORDER BY
-- 	customer.customer_id ASC

-- SELECT f.title
-- FROM film f
-- LEFT JOIN inventory i
--     ON f.film_id = i.film_id
-- WHERE i.film_id IS NULL;

-- SELECT city.city, country.country
-- FROM city
-- INNER JOIN country
-- ON city.country_id = country.country_id

-- SELECT 
-- 	customer.customer_id,
-- 	customer.first_name,
-- 	customer.last_name,
-- 	payment.amount,
-- 	payment.payment_date
-- FROM
-- 	customer
-- INNER JOIN 
-- 	payment
-- ON 
-- 	customer.customer_id = payment.customer_id



