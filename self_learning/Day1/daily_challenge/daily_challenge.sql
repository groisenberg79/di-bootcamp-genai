-- TRUNCATE TABLE actors RESTART IDENTITY

-- INSERT INTO actors(first_name, last_name, birthdate, number_oscars)
-- VALUES
-- 	('Matt', 'Damon', '01/01/1970', 2),
-- 	('George', 'Clooney', '10/22/1965', 1),
-- 	('Meryl', 'Streep', '02/23/1950', 3),
-- 	('Paul', 'Newman', '04/03/1935', 1),
-- 	('Christian', 'Bale', '06/26/1976', 0),
-- 	('Morgan', 'Freeman', '11/19/1952', 2);

-- SELECT COUNT(actor_id)
-- FROM actors

-- INSERT INTO actors(first_name, last_name, number_oscars)
-- VALUES ('Bill', 'Murray', 1)

-- ERROR:  null value in column "birthdate" of relation "actors" violates not-null constraint
-- Failing row contains (8, Bill, Murray, null, 1). 

-- SQL state: 23502
-- Detail: Failing row contains (8, Bill, Murray, null, 1).

-- SELECT first_name AS name_1 FROM actors



