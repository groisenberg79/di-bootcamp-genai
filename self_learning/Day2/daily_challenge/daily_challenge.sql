-- creates table firsttab with fields id (type integer) and name (type varchar with 10 characters)
CREATE TABLE FirstTab (
     id integer, 
     name VARCHAR(10)
)

-- inserts 4 rows into firsttab, where the last row is given a NULL value at the id field
INSERT INTO FirstTab VALUES
(5,'Pawan'),
(6,'Sharlee'),
(7,'Krish'),
(NULL,'Avtaar')

-- selects all rows from firsttab
SELECT * FROM FirstTab

-- creates another table secondtab with only one column id (type integer)
CREATE TABLE SecondTab (
    id integer 
)

-- inserts 2 rows in secondtab with the 2nd being NULL
INSERT INTO SecondTab VALUES
(5),
(NULL)

-- select all rows from secondtab
SELECT * FROM SecondTab

-- Questions

-- Q1. What will be the OUTPUT of the following statement?
-- Answer: 0, because NOT IN evaluates to UNKOWN if there is a NULL in the list, and that's precisely
-- what's happening in NOT IN ( SELECT id FROM SecondTab WHERE id IS NULL ).
-- So every row in FirstTab is discarted.
	SELECT COUNT(*) 
	FROM FirstTab AS ft 
	WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NULL )

-- Q2. What will be the OUTPUT of the following statement?
-- Answer: 2. The subquery SELECT id FROM SecondTab WHERE id = 5 evaluates to the list (5),
-- and 2 rows in FirstTab are such that id is NOT IN (5): (6, Sharlee) and (7, Krish) (note that
-- (NULL, Avtaar) evaluates to UNKOWN, and hence gets discarted).
    SELECT COUNT(*) 
    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id = 5 )

-- Q3. What will be the OUTPUT of the following statement?
-- Answer: 0, for the same reason as Question 1: the subquery (SELECT id FROM SecondTab) evaluates to
-- (5, NULL), and so any NOT IN predicate will evaluate to UNKNOWN.
    SELECT COUNT(*) 
    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab )

-- Q4. What will be the OUTPUT of the following statement?
-- Answer: 2, for the same reason that Question 2 did: the subquery (SELECT id FROM SecondTab WHERE id IS NOT NULL)
-- will evaluate to the list (5).
    SELECT COUNT(*) 
    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NOT NULL )