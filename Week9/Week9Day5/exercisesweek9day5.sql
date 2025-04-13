-- Database: movies

-- DROP DATABASE IF EXISTS movies;
--Exercise 1:
CREATE DATABASE movies
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'French_France.1252'
    LC_CTYPE = 'French_France.1252'
    LOCALE_PROVIDER = 'libc'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

--Task1
SELECT 
    g.genre_name,
    m.title,
    RANK() OVER (PARTITION BY g.genre_name ORDER BY m.popularity DESC) AS popularity_rank
FROM 
    movie m
JOIN 
    movie_genres mg ON m.movie_id = mg.movie_id
JOIN 
    genre g ON mg.genre_id = g.genre_id;

--Task2
SELECT 
    pc.company_name,
    m.title,
    m.revenue,
    NTILE(4) OVER (PARTITION BY pc.company_name ORDER BY m.revenue DESC) AS revenue_quartile
FROM 
    movie m
JOIN 
    movie_company mc ON m.movie_id = mc.movie_id
JOIN 
    production_company pc ON mc.company_id = pc.company_id
WHERE 
    m.revenue IS NOT NULL;

--Task3
SELECT 
    g.genre_name,
    m.title,
    m.budget,
    SUM(m.budget) OVER (
        PARTITION BY g.genre_name 
        ORDER BY m.budget 
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS running_total_budget
FROM 
    movie m
JOIN 
    movie_genres mg ON m.movie_id = mg.movie_id
JOIN 
    genre g ON mg.genre_id = g.genre_id
WHERE 
    m.budget IS NOT NULL
ORDER BY 
    g.genre_name, m.budget;

--Task4
SELECT 
    g.genre_name,
    m.title,
    m.release_date,
    FIRST_VALUE(m.title) OVER (
        PARTITION BY g.genre_name 
        ORDER BY m.release_date DESC
    ) AS most_recent_movie
FROM 
    movie m
JOIN 
    movie_genres mg ON m.movie_id = mg.movie_id
JOIN 
    genre g ON mg.genre_id = g.genre_id
WHERE 
    m.release_date IS NOT NULL;

--Exercise2
--Task1
SELECT 
    actor_stats.person_name,
    DENSE_RANK() OVER (ORDER BY actor_stats.total_movies DESC) AS rank
FROM (
    SELECT 
        p.person_name,
        COUNT(DISTINCT mc.movie_id) AS total_movies
    FROM 
        movie_cast mc
    JOIN 
        person p ON mc.person_id = p.person_id
    GROUP BY 
        p.person_name
) AS actor_stats
ORDER BY rank;

--Task2
WITH director_avg_rating AS (
    SELECT p.person_name AS director_name, 
           AVG(m.vote_average) AS avg_rating
    FROM movie m
    JOIN movie_crew mc ON m.movie_id = mc.movie_id
    JOIN person p ON mc.person_id = p.person_id
    WHERE mc.job = 'Director'
    GROUP BY p.person_name
)
SELECT director_name, avg_rating
FROM director_avg_rating
ORDER BY avg_rating DESC
LIMIT 1;

--Task3
SELECT 
    p.person_name AS actor_name,
    m.title AS movie_title,
    m.revenue,
    SUM(m.revenue) OVER (
        PARTITION BY p.person_name
        ORDER BY m.revenue DESC
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS cumulative_revenue
FROM movie_cast mc
JOIN person p ON mc.person_id = p.person_id
JOIN movie m ON mc.movie_id = m.movie_id
ORDER BY actor_name, cumulative_revenue DESC;

--Task4
WITH director_budgets AS (
    SELECT 
        p.person_name AS director_name,
        SUM(m.budget) AS total_budget
    FROM movie_crew mc
    JOIN person p ON mc.person_id = p.person_id
    JOIN movie m ON mc.movie_id = m.movie_id
    WHERE mc.job = 'Director'
    GROUP BY p.person_name
),
ranked_directors AS (
    SELECT *,
           RANK() OVER (ORDER BY total_budget DESC) AS rank
    FROM director_budgets
)
SELECT director_name, total_budget
FROM ranked_directors
WHERE rank = 1;