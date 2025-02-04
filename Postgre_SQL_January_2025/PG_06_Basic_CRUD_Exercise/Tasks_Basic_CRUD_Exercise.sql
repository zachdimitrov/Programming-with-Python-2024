-- 01. Select Cities
SELECT * FROM cities
ORDER BY id

-- 02. Concatenate
SELECT
    concat(name, ' ', state) AS cities_information,
    area AS area_km2
FROM cities
ORDER BY id

-- 03. Remove Duplicates
SELECT DISTINCT
    name, 
    area AS area_km2
FROM cities
ORDER BY name DESC

-- 04. Limit Records
SELECT 
    id, 
    concat(first_name, ' ', last_name) AS full_name,
    job_title
FROM employees
ORDER BY first_name
LIMIT 50

-- 05. Skip Rows
SELECT
    id AS id, 
    concat(first_name, ' ', middle_name, ' ', last_name) AS full_name,
    hire_date
FROM employees
ORDER BY hire_date
OFFSET 9

-- 06. 
SELECT 
    id,
    concat(number, ' ', street) AS address, 
    city_id
FROM addresses
WHERE id >= 20

-- 07. Positive Even Number
SELECT 
    concat(number, ' ', street) AS address, 
    city_id
FROM addresses
WHERE city_id >= 0 AND city_id % 2 = 0
ORDER BY city_id

-- 08. Projects Data Range
SELECT
    name,
    start_date,
    end_date
FROM projects
WHERE start_date >= '2016-06-01 07:00:00' AND end_date <'2023-06-04 00:00:00'
ORDER BY start_date

-- 09. Multiple Conditions
SELECT
    number,
    street
FROM addresses
WHERE (id >= 50 AND id <= 100) OR number < 1000

-- 10. Set of Values
SELECT
    employee_id,
    project_id
FROM employees_projects
WHERE (employee_id in (200, 250)) AND (project_id NOT IN (50, 100))

-- 11. Compare Char Values
SELECT
    name,
    start_date
FROM projects
WHERE name IN ('Mountain', 'Road', 'Touring')
LINIT 20

-- 12. Salary
SELECT
    concat(first_name, ' ', last_name) AS full_name,
    job_title,
    salary
FROM employees
WHERE salary IN (12500, 14000, 23600, 25000)
ORDER BY salary DESC

-- 13. Missing Value
SELECT
    id,
    first_name,
    last_name
FROM employees
WHERE middle_name IS NULL
LIMIT 3

-- 14. Insert Departments
INSERT INTO departments(department, manager_id)
VALUES
    ('Finance', 3),
    ('Information Services', 42),
    ('Document Control', 90),
    ('Quality Assurance', 274),
    ('Facilities and Maintenance', 218),
    ('Shipping and Receiving', 85),
    ('Executive', 109);

-- 15. New Table
CREATE TABLE company_chart
AS SELECT 
    concat(first_name, ' ', last_name) AS full_name,
    job_title, 
    department_id,
    manager_id
FROM employees;

-- 16. Update Project End Date
UPDATE projects
SET end_date = start_date + INTERVAL '5 month'
WHERE end_date IS NULL

-- 17. Award Experienced
UPDATE employees
SET 
    job_title = concat('Senior ', job_title), 
    salary = salary + 1500
WHERE hire_date >= '1998-01-01' AND hire_date <= '2000-01-05'

-- 18. Delete Addresses
DELETE FROM addresses
WHERE city_id IN (5, 17, 20, 30)

-- 19. Create View
CREATE VIEW view_company_chart AS
SELECT
    full_name,
    job_title
FROM company_chart
WHERE manager_id = 184

SELECT * FROM view_company_chart

-- 20. View Miltiple Tables
CREATE VIEW view_addresses AS
SELECT 
    concat(e.first_name, ' ', e.last_name) AS full_name,
    e.department_id,
    concat(a.number, ' ', a.street) AS address
FROM 
    employees AS e,
    addresses AS a
WHERE e.address_id = a.id

-- 21. Alter View
ALTER VIEW view_addresses
RENAME TO view_employee_addresses_info

-- 22. Drop View
DROP VIEW view_company_chart

-- 23. *Upper
UPDATE projects
SET name = UPPER(name)

-- 24. *Substring
CREATE VIEW view_initials AS
SELECT
    SUBSTRING(first_name, 1, 2) AS initial,
    last_name
FROM employees
ORDER BY last_name;
                                                                                                                                                                                                                            
SELECT * FROM view_initials

ALTER VIEW view_initials
RENAME COLUMN initials TO initial

-- 25. *Like
SELECT
    name,
    start_date
FROM projects
WHERE name LIKE 'MOUNT%'
ORDER BY id