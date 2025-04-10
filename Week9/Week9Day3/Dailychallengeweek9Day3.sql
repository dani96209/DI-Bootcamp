-- Database: Dailychallenge

-- DROP DATABASE IF EXISTS "Dailychallenge";

CREATE DATABASE "Dailychallenge"
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'French_France.1252'
    LC_CTYPE = 'French_France.1252'
    LOCALE_PROVIDER = 'libc'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;



CREATE TABLE Customer (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL
);

CREATE TABLE Customer_profile (
    id SERIAL PRIMARY KEY,
    isLoggedIn BOOLEAN DEFAULT FALSE,
    customer_id INT UNIQUE,  -- Ensures one-to-one relationship
    FOREIGN KEY (customer_id) REFERENCES Customer(id) ON DELETE CASCADE
);

INSERT INTO Customer (first_name, last_name)
VALUES 
('John', 'Doe'),
('Jerome', 'Lalu'),
('Lea', 'Rive');

-- Insert customer profiles
INSERT INTO Customer_profile (isLoggedIn, customer_id)
VALUES
    (TRUE, (SELECT id FROM Customer WHERE first_name = 'John' AND last_name = 'Doe')),
    (FALSE, (SELECT id FROM Customer WHERE first_name = 'Jerome' AND last_name = 'Lalu'));

SELECT c.first_name
FROM Customer c
INNER JOIN Customer_profile cp ON c.id = cp.customer_id
WHERE cp.isLoggedIn = TRUE;

SELECT c.first_name, COALESCE(cp.isLoggedIn, FALSE) AS isLoggedIn
FROM Customer c
LEFT JOIN Customer_profile cp ON c.id = cp.customer_id;

SELECT COUNT(*) 
FROM Customer c
LEFT JOIN Customer_profile cp ON c.id = cp.customer_id
WHERE cp.isLoggedIn = FALSE OR cp.isLoggedIn IS NULL;

CREATE TABLE Book (
    book_id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL
);

INSERT INTO Book (title, author)
VALUES
    ('Alice In Wonderland', 'Lewis Carroll'),
    ('Harry Potter', 'J.K Rowling'),
    ('To kill a mockingbird', 'Harper Lee');

CREATE TABLE Student (
    student_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE,
    age INT CHECK (age <= 15)
);

INSERT INTO Student (name, age)
VALUES
    ('John', 12),
    ('Lera', 11),
    ('Patrick', 10),
    ('Bob', 14);


CREATE TABLE Library (
    book_fk_id INT,
    student_fk_id INT,
    borrowed_date DATE,
    PRIMARY KEY (book_fk_id, student_fk_id),
    FOREIGN KEY (book_fk_id) REFERENCES Book(book_id) 
        ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (student_fk_id) REFERENCES Student(student_id) 
        ON DELETE CASCADE ON UPDATE CASCADE
);


-- John borrowed Alice In Wonderland on 15/02/2022
INSERT INTO Library (book_fk_id, student_fk_id, borrowed_date)
VALUES
    ((SELECT book_id FROM Book WHERE title = 'Alice In Wonderland'), 
     (SELECT student_id FROM Student WHERE name = 'John'),
     '2022-02-15');

-- Bob borrowed To kill a mockingbird on 03/03/2021
INSERT INTO Library (book_fk_id, student_fk_id, borrowed_date)
VALUES
    ((SELECT book_id FROM Book WHERE title = 'To kill a mockingbird'), 
     (SELECT student_id FROM Student WHERE name = 'Bob'),
     '2021-03-03');

-- Lera borrowed Alice In Wonderland on 23/05/2021
INSERT INTO Library (book_fk_id, student_fk_id, borrowed_date)
VALUES
    ((SELECT book_id FROM Book WHERE title = 'Alice In Wonderland'), 
     (SELECT student_id FROM Student WHERE name = 'Lera'),
     '2021-05-23');

-- Bob borrowed Harry Potter on 12/08/2021
INSERT INTO Library (book_fk_id, student_fk_id, borrowed_date)
VALUES
    ((SELECT book_id FROM Book WHERE title = 'Harry Potter'), 
     (SELECT student_id FROM Student WHERE name = 'Bob'),
     '2021-08-12');


SELECT * FROM Library;


SELECT s.name AS student_name, b.title AS book_title
FROM Library l
JOIN Student s ON l.student_fk_id = s.student_id
JOIN Book b ON l.book_fk_id = b.book_id;

SELECT AVG(s.age) AS average_age
FROM Library l
JOIN Student s ON l.student_fk_id = s.student_id
JOIN Book b ON l.book_fk_id = b.book_id
WHERE b.title = 'Alice In Wonderland';


DELETE FROM Student WHERE name = 'John';

--ON DELETE CASCADE: Since the Library table was created with foreign keys that have the ON DELETE CASCADE constraint, when a student is deleted from the Student table, all records in the Library table that reference this student (via student_fk_id) will also be automatically deleted. This ensures that any borrow records associated with the deleted student are removed as well.

--So, when you delete the student "John", all the records in the Library table where student_fk_id corresponds to "John" will also be deleted.
