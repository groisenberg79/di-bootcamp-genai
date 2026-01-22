-- PART I

-- Create 2 tables : Customer and Customer profile. They have a One to One relationship.
-- A customer can have only one profile, and a profile belongs to only one customer
-- The Customer table should have the columns : id, first_name, last_name NOT NULL
-- The Customer profile table should have the columns : id, isLoggedIn DEFAULT false (a Boolean), customer_id (a reference to the Customer table)

-- CREATE TABLE customer(
-- 	id SERIAL PRIMARY KEY NOT NULL,
-- 	first_name VARCHAR(50) NOT NULL,
-- 	last_name VARCHAR(50) NOT NULL
-- )

-- CREATE TABLE customer_profile(
-- 	id SERIAL PRIMARY KEY NOT NULL,
-- 	is_logged_in BOOLEAN DEFAULT false NOT NULL,
-- 	customer_id INTEGER UNIQUE NOT NULL,

-- 	CONSTRAINT customer_profile_customer_id_fkey
-- 		FOREIGN KEY (customer_id)
-- 		REFERENCES customer(id)
-- 		ON DELETE CASCADE
-- )

-- Insert those customers
-- 		John, Doe
-- 		Jerome, Lalu
-- 		Lea, Rive

-- INSERT INTO customer(first_name, last_name)
-- VALUES
-- 	('John', 'Doe'),
-- 	('Jerome', 'Lau'),
-- 	('Lea', 'Rive')

-- Insert those customer profiles, use subqueries
-- 		John is loggedIn
-- 		Jerome is not logged in

-- INSERT INTO customer_profile(is_logged_in, customer_id)
-- VALUES
-- 	(true, (SELECT id FROM customer WHERE first_name = 'John')),
-- 	(false, (SELECT id FROM customer WHERE first_name = 'Jerome'))

-- Use the relevant types of Joins to display:
-- 		The first_name of the LoggedIn customers
-- 		All the customers first_name and isLoggedIn columns - even the customers those who don’t have a profile.
-- 		The number of customers that are not LoggedIn

-- SELECT c.first_name 
-- FROM customer c
-- INNER JOIN customer_profile cp ON c.id = cp.customer_id
-- 	WHERE cp.is_logged_in = true

-- SELECT c.first_name, cp.is_logged_in
-- FROM customer c
-- LEFT JOIN customer_profile cp ON c.id = cp.customer_id

-- SELECT COUNT(*) AS not_logged_in
-- FROM customer c
-- INNER JOIN customer_profile cp ON c.id = cp.customer_id
-- 	WHERE cp.is_logged_in = false

-- PART II

