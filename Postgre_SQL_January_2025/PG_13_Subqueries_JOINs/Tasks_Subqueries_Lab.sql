/*
JOINs
-----
INNER JOIN (JOIN) - samo obshtite rezultati
LEFT JOIN - vsichko ot lqvata tablica + obshtite ot dqsnata
RIGHT JOIN - obratnoto
FULL JOIN - vsichki danni - kydeto ne se pripokrivata e NULL
CROSS JOIN - combine every left with every right (no ON clause)
*/

SELECT
    *
FROM persons AS p
    LEFT JOIN countries as c ON p.country.id = c.id
ORDER BY country_id DESC

-- 01. 
SELECT 
    t.town_id,
    t.name,
    a.address_text as town_name
FROM towns as t 
    JOIN addresses AS a ON t.town_id = a.town_id -- USING (town_id)
WHERE t.name IN('San Francisco', 'Sofia', 'Carnation')
ORDER BY t.town_id, a.address_id;

-- 02. 
SELECT
    e.employee_id,
    concat(e.first_name, ' ', e.last_name) AS full_name,
    d.department_id,
    d.name
FROM employees AS e
    JOIN departments AS d ON e.employee_id = d.manager_id
ORDER BY e.employee_id
LIMIT 5;

-- 03.
SELECT 
    e.employee_id,
    concat(e.first_name, ' ', e.last_name) AS full_name,
    p.project_id,
    p.name
FROM employees AS e 
    JOIN employees_projects AS ep ON e.employee_id = ep.employee_id
        JOIN projects as p ON ep.project_id = p.project_id
WHERE p.project_id = 1

/*
Subqueries
----------
used to get value from table to use in other cases
*/

INSERT INTO persons (id, first_name, last_name, country_id)
VALUES 
    (1001, 'Milko', 'Gatev', (SELECT id FROM countries WHERE country = 'Spain')),
    (1002, 'Gosho', 'Petkov', (SELECT id FROM countries WHERE country = 'Bulgaria'));

SELECT 
    *
FROM persons
WHERE country_id = (SELECT id FROM countries WHERE country = 'Bulgaria')

ALTER TABLE persons
ADD COLUMN salary int DEFAULT 0
UPDATE persons
SET salary = floor(random() * 10000) + 1;

SELECT min(avg_salary)
FROM
    (SELECT AVG(salary) AS avg_salary FROM persons GROUP BY country_id)

-- 04.
SELECT COUNT(*) FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees)

-- Index
-- Cluster Index - only primary key (sorted)
-- Not Cluster index - like book 

CREATE INDEX first_name_idx ON people(first_name)
SELECT pg_size_pretty(pg_relation_size('first_name_idx'))
SELECT pg_size_pretty(pg_relation_size('people'))

