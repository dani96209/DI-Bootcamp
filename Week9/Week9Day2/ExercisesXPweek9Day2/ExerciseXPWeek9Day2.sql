-- Table: public.items

-- DROP TABLE IF EXISTS public.items;

CREATE TABLE IF NOT EXISTS public.items
( id SERIAL PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  price INT NOT NULL
);

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.items
    OWNER to postgres;

INSERT INTO public.items (name, price) VALUES
('Small Desk', 100),
('Large Desk', 300),
('Fan', 80);

CREATE TABLE IF NOT EXISTS public.customers
( id SERIAL PRIMARY KEY,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL
);

INSERT INTO public.customers (first_name, last_name) VALUES
('Greg', 'Jones'),
('Sandra', 'Jones'),
('Scott', 'Scott'),
('Trevor', 'Green'),
('Melanie', 'Johnson');

SELECT * FROM public.items;

SELECT * FROM public.items
WHERE price > 80;

SELECT * FROM public.items
WHERE price <= 300;

SELECT * FROM public.customers
WHERE last_name = 'Smith';

SELECT * FROM public.customers
WHERE last_name = 'Jones';

SELECT * FROM public.customers
WHERE first_name != 'Scott';

SELECT * FROM public.items 
ORDER BY price ASC;

SELECT * FROM public.items 
WHERE price >= 80 
ORDER BY price DESC;

SELECT first_name, last_name FROM public.customers 
ORDER BY first_name ASC 
LIMIT 3;

SELECT last_name FROM public.customers 
ORDER BY last_name DESC;


