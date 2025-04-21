select date from salaries;

--Exercise1:
CREATE TABLE df_employee AS
SELECT 
    s.employee_id || '_' || CAST(s.date AS TEXT) AS id,
    strftime('%Y-%m', 
    SUBSTR(s.date, 7, 4) || '-' || SUBSTR(s.date, 4, 2) || '-' || SUBSTR(s.date, 1, 2)
) AS month_year,
    s.employee_id,
    s.employee_name,
    e."GEN(M_F)" AS gender,
    e.age,
    s.salary,
    f.function_group,
    c.company_name,
    c.company_city,
    c.company_state,
    c.company_type,
    c.const_site_category
FROM employees e
LEFT JOIN salaries s ON e.employee_name_emp = s.employee_name
LEFT JOIN functions f ON s.func_code = f.function_code
LEFT JOIN companies c ON s.comp_name = c.company_name;

--Exercise2:
select* from df_employee;


UPDATE df_employee
SET
    id = TRIM(id),
    month_year = TRIM(month_year),
    employee_id = TRIM(employee_id),
    employee_name = TRIM(employee_name),
    gender = TRIM(gender),
    function_group = TRIM(function_group),
    company_name = TRIM(company_name),
    company_city = TRIM(company_city),
    company_state = TRIM(company_state),
    company_type = TRIM(company_type),
    const_site_category = TRIM(const_site_category);
    
    
    SELECT *
FROM df_employee
WHERE id IS NULL OR id = ''
   OR month_year IS NULL OR month_year = ''
   OR employee_id IS NULL OR employee_id = ''
   OR employee_name IS NULL OR employee_name = ''
   OR gender IS NULL OR gender = ''
   OR function_group IS NULL OR function_group = ''
   OR company_name IS NULL OR company_name = ''
   OR company_city IS NULL OR company_city = ''
   OR company_state IS NULL OR company_state = ''
   OR company_type IS NULL OR company_type = ''
   OR const_site_category IS NULL OR const_site_category = '';
   
DELETE FROM df_employee
WHERE id IS NULL OR id = ''
   OR month_year IS NULL OR month_year = ''
   OR employee_id IS NULL OR employee_id = ''
   OR employee_name IS NULL OR employee_name = ''
   OR gender IS NULL OR gender = ''
   OR function_group IS NULL OR function_group = ''
   OR company_name IS NULL OR company_name = ''
   OR company_city IS NULL OR company_city = ''
   OR company_state IS NULL OR company_state = ''
   OR company_type IS NULL OR company_type = ''
   OR const_site_category IS NULL OR const_site_category = '';
   
 select* from df_employee;
 
 --Exercise3:
 
 SELECT 
    company_name,
    COUNT(DISTINCT employee_id) AS current_employee_count
FROM df_employee
WHERE month_year = (
    SELECT MAX(month_year) FROM df_employee
)
GROUP BY company_name
ORDER BY current_employee_count DESC;

--Exercise 4:
WITH city_counts AS (
    SELECT 
        company_city,
        COUNT(DISTINCT employee_id) AS employee_count
    FROM df_employee
    GROUP BY company_city
),
total AS (
    SELECT SUM(employee_count) AS total_count FROM city_counts
)
SELECT 
    c.company_city,
    c.employee_count,
    ROUND(100.0 * c.employee_count / t.total_count, 2) AS percentage
FROM city_counts c
JOIN total t
ORDER BY percentage DESC;

SELECT 
    month_year,
    COUNT(DISTINCT employee_id) AS employee_count
FROM df_employee
GROUP BY month_year
ORDER BY month_year;


WITH monthly_counts AS (
    SELECT 
        month_year,
        COUNT(DISTINCT employee_id) AS employee_count
    FROM df_employee
    GROUP BY month_year
)
SELECT 
    ROUND(AVG(employee_count), 2) AS average_employees_per_month
FROM monthly_counts;

--Exercise5:
WITH monthly_counts AS (
    SELECT 
        month_year,
        COUNT(DISTINCT employee_id) AS employee_count
    FROM df_employee
    GROUP BY month_year
)
SELECT 
    'MIN' AS type,
    month_year,
    employee_count
FROM monthly_counts
WHERE employee_count = (SELECT MIN(employee_count) FROM monthly_counts)

UNION

SELECT 
    'MAX' AS type,
    month_year,
    employee_count
FROM monthly_counts
WHERE employee_count = (SELECT MAX(employee_count) FROM monthly_counts);

WITH monthly_func_counts AS (
    SELECT 
        month_year,
        function_group,
        COUNT(DISTINCT employee_id) AS employee_count
    FROM df_employee
    GROUP BY month_year, function_group
)
SELECT 
    function_group,
    ROUND(AVG(employee_count), 2) AS avg_monthly_employees
FROM monthly_func_counts
GROUP BY function_group
ORDER BY avg_monthly_employees DESC;

SELECT 
    SUBSTR(month_year, 1, 4) AS year,
    ROUND(AVG(salary), 2) AS avg_annual_salary
FROM df_employee
GROUP BY year
ORDER BY year;