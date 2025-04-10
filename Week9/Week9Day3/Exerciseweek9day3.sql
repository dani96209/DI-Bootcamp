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

SELECT name FROM language;

SELECT 
    f.title, 
    f.description, 
    l.name AS language_name
FROM film f
JOIN language l ON f.language_id = l.language_id;

SELECT 
    f.title, 
    f.description, 
    l.name AS language_name
FROM language l
LEFT JOIN film f ON l.language_id = f.language_id;

CREATE TABLE new_film (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

INSERT INTO new_film (name) 
VALUES 
('Matrix'),
('Inception'),
('The Dark Knight');

SELECT * FROM new_film;

CREATE TABLE customer_review (
    review_id SERIAL PRIMARY KEY,         -- Identifiant unique de la revue
    film_id INT NOT NULL,                 -- Référence à l'id du film dans la table new_film
    language_id INT NOT NULL,             -- Référence à l'id de la langue dans la table language
    title VARCHAR(255) NOT NULL,          -- Titre de la revue
    score INT CHECK (score >= 1 AND score <= 10), -- Note de la revue (entre 1 et 10)
    review_text TEXT,                     -- Texte de la revue (pas de limite de longueur)
    last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Dernière mise à jour de la revue
    CONSTRAINT fk_film FOREIGN KEY (film_id) REFERENCES new_film(id) ON DELETE CASCADE,  -- Suppression en cascade des revues si un film est supprimé
    CONSTRAINT fk_language FOREIGN KEY (language_id) REFERENCES language(language_id)    -- Référence à la table language
);

INSERT INTO customer_review (film_id, language_id, title, score, review_text)
VALUES 
(1, 1, 'Amazing Movie!', 9, 'This film was a thrilling experience. The plot and action were excellent!'),
(2, 2, 'Good but slow', 7, 'While the movie had some interesting moments, it was a bit too slow for my taste.');

SELECT * FROM customer_review;

SELECT 
    cr.review_id, 
    cr.film_id, 
    f.name AS film_name, 
    cr.language_id, 
    l.name AS language_name, 
    cr.title, 
    cr.score, 
    cr.review_text, 
    cr.last_update
FROM customer_review cr
JOIN language l ON cr.language_id = l.language_id
JOIN new_film f ON cr.film_id = f.id;

DELETE FROM new_film WHERE id = 1;

SELECT * FROM customer_review;

--Exercise 2

UPDATE film
SET language_id = 2  -- Remplace par un ID valide de la table "language"
WHERE film_id IN (10, 20, 30);  -- Remplace par les ID des films que tu veux modifier

--Foreign Keys (References) in the customer Table – dvdrental Database
--The customer table in the dvdrental database contains foreign keys that enforce relationships with other tables. Based on the standard schema of dvdrental, here are the foreign keys:

--Foreign Keys in the customer Table
--store_id → References store(store_id)

--Each customer belongs to a specific store.

--address_id → References address(address_id)

--Dependencies Must Exist

--When inserting a new customer, the store_id and address_id must reference existing values in the store and address tables.

--If we try to insert a customer with a store_id or address_id that does not exist, the INSERT will fail due to foreign key constraints.

--Order of Inserts Matters

--We must first insert the required store in the store table and the address in the address table before inserting into the customer table

--Each customer has an address, which is stored in the address table.



SELECT COUNT(*) AS outstanding_rentals
FROM rental
WHERE return_date IS NULL;

select * from rental where return_date is null;

SELECT f.film_id, f.title, f.rental_rate, r.rental_date
FROM rental r
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
WHERE r.return_date IS NULL
ORDER BY f.rental_rate DESC
LIMIT 30;

SELECT f.film_id, f.title, f.description
FROM film f
JOIN film_actor fa ON f.film_id = fa.film_id
JOIN actor a ON fa.actor_id = a.actor_id
WHERE f.description ILIKE '%sumo%'
AND a.first_name = 'Penelope' AND a.last_name = 'Monroe';

SELECT film_id, title, description, length, rating
FROM film
WHERE length < 60
AND rating = 'R';

SELECT f.film_id, f.title, f.description, p.amount, r.return_date
FROM customer c
JOIN rental r ON c.customer_id = r.customer_id
JOIN payment p ON r.rental_id = p.rental_id
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
WHERE c.first_name = 'Matthew' 
AND c.last_name = 'Mahan'
AND p.amount > 4.00
AND r.return_date BETWEEN '2005-07-28' AND '2005-08-01';

SELECT f.film_id, f.title, f.description, f.replacement_cost
FROM customer c
JOIN rental r ON c.customer_id = r.customer_id
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
WHERE c.first_name = 'Matthew'
AND c.last_name = 'Mahan'
AND (f.title ILIKE '%boat%' OR f.description ILIKE '%boat%')
ORDER BY f.replacement_cost DESC
LIMIT 1;
