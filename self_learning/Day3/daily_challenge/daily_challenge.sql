-- PART I

-- Create 2 tables : Customer and Customer profile. They have a One to One relationship.
-- A customer can have only one profile, and a profile belongs to only one customer
-- The Customer table should have the columns : id, first_name, last_name NOT NULL
-- The Customer profile table should have the columns : id, isLoggedIn DEFAULT false (a Boolean), customer_id (a reference to the Customer table)

CREATE TABLE customer(
	id SERIAL PRIMARY KEY NOT NULL,
	first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50) NOT NULL
);

CREATE TABLE customer_profile(
	id SERIAL PRIMARY KEY NOT NULL,
	is_logged_in BOOLEAN DEFAULT false NOT NULL,
	customer_id INTEGER UNIQUE NOT NULL,

	CONSTRAINT customer_profile_customer_id_fkey
		FOREIGN KEY (customer_id)
		REFERENCES customer(id)
		ON DELETE CASCADE
);

-- Insert those customers
-- 		John, Doe
-- 		Jerome, Lalu
-- 		Lea, Rive

INSERT INTO customer(first_name, last_name)
VALUES
	('John', 'Doe'),
	('Jerome', 'Lau'),
	('Lea', 'Rive');

-- Insert those customer profiles, use subqueries
-- 		John is loggedIn
-- 		Jerome is not logged in

INSERT INTO customer_profile(is_logged_in, customer_id)
VALUES
	(true, (SELECT id FROM customer WHERE first_name = 'John')),
	(false, (SELECT id FROM customer WHERE first_name = 'Jerome'));

-- Use the relevant types of Joins to display:
-- 		The first_name of the LoggedIn customers
-- 		All the customers first_name and isLoggedIn columns - even the customers those who don’t have a profile.
-- 		The number of customers that are not LoggedIn

SELECT c.first_name 
FROM customer c
INNER JOIN customer_profile cp ON c.id = cp.customer_id
	WHERE cp.is_logged_in = true;

SELECT c.first_name, cp.is_logged_in
FROM customer c
LEFT JOIN customer_profile cp ON c.id = cp.customer_id;

SELECT COUNT(*) AS not_logged_in
FROM customer c
INNER JOIN customer_profile cp ON c.id = cp.customer_id
	WHERE cp.is_logged_in = false;

-- PART II

-- Create a table named Book, with the columns :
-- book_id SERIAL PRIMARY KEY, title NOT NULL, author NOT NULL

CREATE TABLE books(
	book_id SERIAL PRIMARY KEY,
	title VARCHAR(100) NOT NULL,
	author VARCHAR(100) NOT NULL
);

-- Insert those books :
-- 		Alice In Wonderland, Lewis Carroll
-- 		Harry Potter, J.K Rowling
-- 		To kill a mockingbird, Harper Lee

INSERT INTO books (title, author)
VALUES
	('Alice In Wonderland', 'Lewis Caroll'),
	('Harry Potter', 'J. K. Rowling'),
	('To Kill a Mockingbird', 'Harper Lee');

-- Create a table named Student, with the columns : 
-- student_id SERIAL PRIMARY KEY, name NOT NULL UNIQUE, age. 
-- Make sure that the age is never bigger than 15 (Find an SQL method);

CREATE TABLE students(
	student_id SERIAL PRIMARY KEY,
	name VARCHAR(100) NOT NULL UNIQUE,
	age INTEGER NOT NULL,

	CONSTRAINT students_age_max_chk CHECK (age <= 15)
);

-- Insert those students:
-- John, 12
-- Lera, 11
-- Patrick, 10
-- Bob, 14

INSERT INTO students(name, age)
VALUES
	('John', 12),
	('Lera', 11),
	('Patrick', 10),
	('Bob', 14);

-- Create a table named Library, with the columns :
-- book_fk_id ON DELETE CASCADE ON UPDATE CASCADE
-- student_id ON DELETE CASCADE ON UPDATE CASCADE
-- borrowed_date
-- This table, is a junction table for a Many to Many relationship with the Book and Student tables : A student can borrow many books, and a book can be borrowed by many children
-- book_fk_id is a Foreign Key representing the column book_id from the Book table
-- student_fk_id is a Foreign Key representing the column student_id from the Student table
-- The pair of Foreign Keys is the Primary Key of the Junction Table

CREATE TABLE library(
	book_fk_id INTEGER NOT NULL,
	student_fk_id INTEGER NOT NULL,
	borrowed_date DATE NOT NULL,

	CONSTRAINT library_book_fk_id_fkey 
		FOREIGN KEY (book_fk_id) REFERENCES books(book_id)
		ON DELETE CASCADE 
		ON UPDATE CASCADE,

	CONSTRAINT library_student_fk_id_fkey
		FOREIGN KEY (student_fk_id) REFERENCES students(student_id)
		ON DELETE CASCADE
		ON UPDATE CASCADE
);

-- Add 4 records in the junction table, use subqueries.
-- 		the student named John, borrowed the book Alice In Wonderland on the 15/02/2022
-- 		the student named Bob, borrowed the book To kill a mockingbird on the 03/03/2021
-- 		the student named Lera, borrowed the book Alice In Wonderland on the 23/05/2021
-- 		the student named Bob, borrowed the book Harry Potter the on 12/08/2021

INSERT INTO library(book_fk_id, student_fk_id, borrowed_date)
VALUES
	((SELECT book_id FROM books b WHERE b.title = 'Alice In Wonderland'),
	(SELECT student_id FROM students s WHERE s.name = 'John'), 
	'2022-02-15'),
	((SELECT book_id FROM books b WHERE b.title = 'To Kill a Mockingbird'),
	(SELECT student_id FROM students s WHERE s.name = 'Bob'), 
	'2021-03-03'),
	((SELECT book_id FROM books b WHERE b.title = 'Alice In Wonderland'),
	(SELECT student_id FROM students s WHERE s.name = 'Lera'),
	'2021-05-23'),
	((SELECT book_id FROM books b WHERE b.title = 'Harry Potter'),
	(SELECT student_id FROM students s WHERE s.name = 'Bob'),
	'2021-08-12');

-- Display the data
-- 		Select all the columns from the junction table
-- 		Select the name of the student and the title of the borrowed books
-- 		Select the average age of the children, that borrowed the book Alice in Wonderland
-- 		Delete a student from the Student table, what happened in the junction table ?

SELECT * FROM library;

SELECT s.name, b.title
FROM students s
INNER JOIN library lib ON s.student_id = lib.student_fk_id
INNER JOIN books b ON lib.book_fk_id = b.book_id

SELECT AVG(s.age)
FROM students s
WHERE s.student_id IN (SELECT lib.student_fk_id FROM library lib);

DELETE FROM students WHERE students.name = 'John';

-- now the library table will have one less row: the one corresponding to the student named 'John'.

SELECT * FROM library;
	