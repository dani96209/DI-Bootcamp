-- Database: dvdrental

-- DROP DATABASE IF EXISTS dvdrental;

CREATE DATABASE dvdrental
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'French_France.1252'
    LC_CTYPE = 'French_France.1252'
    LOCALE_PROVIDER = 'libc'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

SELECT * 
FROM customer;

SELECT 
    first_name || ' ' || last_name AS full_name
FROM customer;

SELECT DISTINCT create_date
FROM customer;

SELECT *
FROM customer
ORDER BY first_name DESC;

SELECT film_id, title, description, release_year, rental_rate
FROM film
ORDER BY rental_rate ASC;

SELECT a.address, a.phone
FROM address a
JOIN customer c ON a.address_id = c.address_id
WHERE a.district = 'Texas';

SELECT *
FROM film
WHERE film_id IN (15, 150);


SELECT film_id, title, description, length, rental_rate
FROM film
WHERE title = 'Equilibrium';

SELECT film_id, title, description, length, rental_rate
FROM film
WHERE title LIKE 'Eq%';

SELECT film_id, title, rental_rate
FROM film
ORDER BY rental_rate ASC
LIMIT 10;

SELECT film_id, title, rental_rate
FROM film
ORDER BY rental_rate ASC
OFFSET 10 ROWS
FETCH NEXT 10 ROWS ONLY;

SELECT c.first_name, c.last_name, p.amount, p.payment_date
FROM customer c
JOIN payment p ON c.customer_id = p.customer_id
ORDER BY c.customer_id ASC;

SELECT f.film_id, f.title
FROM film f
LEFT JOIN inventory i ON f.film_id = i.film_id
WHERE i.inventory_id IS NULL;

SELECT city.city, country.country
FROM city
JOIN country ON city.country_id = country.country_id;

SELECT c.customer_id, c.first_name, c.last_name, p.amount, p.payment_date, p.staff_id
FROM customer c
JOIN payment p ON c.customer_id = p.customer_id
ORDER BY p.staff_id ASC;