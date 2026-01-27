CREATE SCHEMA restaurant
AUTHORIZATION gabrielroisenbergrodrigues;

CREATE TABLE restaurant.menu_items(
    item_id SERIAL PRIMARY KEY,
    item_name VARCHAR(30) NOT NULL UNIQUE,
    item_price SMALLINT DEFAULT 0
);