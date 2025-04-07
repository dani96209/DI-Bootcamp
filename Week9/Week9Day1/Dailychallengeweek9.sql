-- Database: Hollywood

-- DROP DATABASE IF EXISTS "Hollywood";

CREATE DATABASE "Hollywood"
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'French_France.1252'
    LC_CTYPE = 'French_France.1252'
    LOCALE_PROVIDER = 'libc'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

CREATE TABLE actors(
 actor_id SERIAL PRIMARY KEY,
 first_name VARCHAR (50) NOT NULL,
 last_name VARCHAR (100) NOT NULL,
 age DATE NOT NULL,
 number_oscars SMALLINT NOT NULL
);

INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES
('George', 'Clooney', '06/05/1961', 2),
('Brad', 'Pitt', '18/12/1963', 1),
('Meryl', 'Streep', '22/06/1949', 3),
('Leonardo', 'DiCaprio', '11/11/1974', 1),
('Julia', 'Roberts', '28/10/1967', 1),
('Tom', 'Hanks', '09/07/1956', 2),
('Denzel', 'Washington', '28/12/1954', 2);

SELECT COUNT(*) FROM actors;

INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES (NULL, NULL, NULL, NULL);
-- If we try to add an actor with empty fields in columns with a NOT NULL constraint, the insert will fail.
