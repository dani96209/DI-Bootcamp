
--Exercises
--Exercise 1
--Task 1
SELECT m.medal_name, 
       (SELECT AVG(g.age) 
        FROM games_competitor g
        WHERE g.id IN (
            SELECT ce.competitor_id 
            FROM competitor_event ce 
            WHERE ce.medal_id = m.id
        )
       ) AS average_age
FROM medal m;

--Task 2
SELECT nr.region_name, COUNT(DISTINCT competitor_id) AS unique_competitors
FROM (
    -- Find competitors who have participated in more than 3 different events
    SELECT competitor_id
    FROM competitor_event
    GROUP BY competitor_id
    HAVING COUNT(DISTINCT event_id) > 3
) AS filtered_competitors
JOIN games_competitor gc ON filtered_competitors.competitor_id = gc.person_id
JOIN noc_region nr ON gc.id = nr.id
GROUP BY nr.region_name
ORDER BY unique_competitors DESC
LIMIT 5;

--Task 3
CREATE TEMPORARY TABLE temp_medal_winners AS
SELECT competitor_id, COUNT(medal_id) AS total_medals
FROM competitor_event
WHERE medal_id IS NOT NULL  -- Participations without medals are ignored.
GROUP BY competitor_id
HAVING COUNT(medal_id) > 2;

CREATE TEMPORARY TABLE temp_competitor_analysis AS
SELECT competitor_id, COUNT(medal_id) AS total_medals
FROM competitor_event
GROUP BY competitor_id;

--Task 4
DELETE FROM temp_competitor_analysis
WHERE competitor_id IN (
    SELECT competitor_id FROM competitor_event
    GROUP BY competitor_id
    HAVING COUNT(medal_id) = 0
);

SELECT * FROM temp_competitor_analysis;

-- Exercise 2
--Task 1
UPDATE person
SET height = (
    SELECT AVG(p2.height)
    FROM person p2
    JOIN person_region pr2 ON p2.id = pr2.person_id
    WHERE pr2.region_id = person_region.region_id
)
WHERE height IS NULL
AND person.id IN (
    SELECT person_id FROM person_region
);

--Task 2
CREATE TEMPORARY TABLE temp_competitors AS
SELECT competitor_id, games_id, COUNT(DISTINCT event_id) AS total_events
FROM competitor_event
JOIN games_competitor ON competitor_event.competitor_id = games_competitor.id
GROUP BY competitor_id, games_id
HAVING COUNT(DISTINCT event_id) > 1;

SELECT nr.region_name, 
       AVG(competitor_medals.medals_count) AS avg_medals_per_competitor
FROM (
    -- Subquery: Number of medals per competitor and per region
    SELECT pr.region_id, ce.competitor_id, COUNT(ce.medal_id) AS medals_count
    FROM competitor_event ce
    JOIN person_region pr ON ce.competitor_id = pr.person_id
    WHERE ce.medal_id IS NOT NULL
    GROUP BY pr.region_id, ce.competitor_id
) competitor_medals
JOIN noc_region nr ON competitor_medals.region_id = nr.id
GROUP BY nr.region_name
HAVING AVG(competitor_medals.medals_count) > (
    -- Overall average medals per competitor
    SELECT AVG(medals_count) 
    FROM (
        SELECT competitor_id, COUNT(medal_id) AS medals_count
        FROM competitor_event
        WHERE medal_id IS NOT NULL
        GROUP BY competitor_id
    ) overall_avg
)
ORDER BY avg_medals_per_competitor DESC;


-- Task 4
-- Created a temporary table to store competitors and their seasons of participation
CREATE TEMPORARY TABLE temp_competitor_seasons AS
SELECT gc.person_id, 
       MIN(g.season) AS first_season, 
       MAX(g.season) AS last_season
FROM games_competitor gc
JOIN games g ON gc.games_id = g.id
GROUP BY gc.person_id
HAVING MIN(g.season) <> MAX(g.season);

--Dailychallenge

--Exercise1
-- Task 1
-- Creation of a temporary table to store competitors and their medals by season
CREATE TEMPORARY TABLE temp_medalists AS
SELECT gc.person_id, 
       g.season, 
       COUNT(ce.medal_id) AS total_medals
FROM games_competitor gc
JOIN competitor_event ce ON gc.id = ce.competitor_id
JOIN games g ON gc.games_id = g.id
WHERE ce.medal_id IS NOT NULL
GROUP BY gc.person_id, g.season;

-- Selection of competitors who won medals in both seasons
SELECT person_id 
FROM temp_medalists
GROUP BY person_id
HAVING COUNT(DISTINCT season) = 2;

SELECT * FROM temp_medalists;

-- Task 2
-- Create a temporary table to store competitors who have won medals in exactly two sports
CREATE TEMPORARY TABLE temp_two_sport_medalists AS
SELECT ce.competitor_id, 
       COUNT(DISTINCT e.sport_id) AS unique_sports, 
       COUNT(ce.medal_id) AS total_medals
FROM competitor_event ce
JOIN event e ON ce.event_id = e.id
WHERE ce.medal_id IS NOT NULL
GROUP BY ce.competitor_id
HAVING COUNT(DISTINCT e.sport_id) = 2;

-- Select the 3 competitors with the most medals and display the sport names
SELECT tsm.competitor_id, tsm.total_medals, 
       GROUP_CONCAT(DISTINCT s.sport_name) AS sports_played
FROM temp_two_sport_medalists tsm
JOIN competitor_event ce ON tsm.competitor_id = ce.competitor_id
JOIN event e ON ce.event_id = e.id
JOIN sport s ON e.sport_id = s.id
GROUP BY tsm.competitor_id, tsm.total_medals
ORDER BY tsm.total_medals DESC
LIMIT 3;

-- Exercise2
--Task 1
--Step1
WITH competitor_top_event AS (
    SELECT ce.competitor_id, 
           ce.event_id, 
           COUNT(ce.medal_id) AS medal_count
    FROM competitor_event ce
    WHERE ce.medal_id IS NOT NULL
    GROUP BY ce.competitor_id, ce.event_id
    HAVING COUNT(ce.medal_id) = (
        SELECT MAX(medal_total)
        FROM (
            SELECT COUNT(ce2.medal_id) AS medal_total
            FROM competitor_event ce2
            WHERE ce2.competitor_id = ce.competitor_id AND ce2.medal_id IS NOT NULL
            GROUP BY ce2.event_id
        ) AS event_medals
    )
)

-- Step 2: Match competitors to regions and total medals by region
SELECT nr.region_name, 
       SUM(cte.medal_count) AS total_medals
FROM competitor_top_event cte
JOIN games_competitor gc ON cte.competitor_id = gc.id
JOIN person_region pr ON gc.person_id = pr.person_id
JOIN noc_region nr ON pr.region_id = nr.id
GROUP BY nr.region_name
ORDER BY total_medals DESC
LIMIT 5;

-- Task 2
-- Create a temporary table to store eligible competitors
CREATE TEMP TABLE temp_no_medal_competitors AS
SELECT gc.person_id, p.full_name, COUNT(DISTINCT gc.games_id) AS games_participated
FROM games_competitor gc
JOIN person p ON gc.person_id = p.id
LEFT JOIN competitor_event ce ON gc.id = ce.competitor_id
WHERE ce.medal_id IS NULL
GROUP BY gc.person_id, p.full_name
HAVING COUNT(DISTINCT gc.games_id) > 3;

-- Displaying the contents of the temporary table
SELECT * FROM temp_no_medal_competitors;

