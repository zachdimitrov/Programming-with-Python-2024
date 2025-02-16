SELECT 'Hitar'
' '
'Petar' -- result 'Hitar Petar'

SELECT 'Can''t' -- ' escapes special symbols

CREATE TABLE my_test_table (
    id SERIAL PRIMARY KEY,
    "Create" VARCHAT(30), -- escape special words
    "Name" VARCHAR(40) -- add case sensitive
    salary DECIMAL(5, 2)
)

SELECT sAlARy FROM my_test_table -- case insensitive
SELECT Name FROM my_test_table; -- case sensitive

/*
this is a
multiline
comment
*/

--01. Retrieving Data
-- select all
SELECT * FROM employees;

-- select specific columns
SELECT 
    first_name,
    last_name,
    department 
FROM
    employees;

-- with alias
SELECT 
    e.first_name AS "First Name",
    e.last_name AS "Last Name"
FROM
    employees AS e

/* HOMEWORK */

--01.
SELECT 
    e.id,
    concat(e.first_name, ' ', e.last_name) AS "Full Name",
    e.job_title AS "Job Title"
FROM
    employees AS e
ORDER BY id

--02.
SELECT
    e.id,
    concat(e.first_name, ' ', e.last_name) AS full_name,
    e.job_title,
    e.salary
FROM    
    employees AS e
WHERE 
    e.salary >= 1000;


--02A. Richest
SELECT
    e.id,
    concat(e.first_name, ' ', e.last_name) AS full_name,
    e.salary
FROM employees AS e
ORDER BY salary DESC
LIMIT 3

--02B. Distinct
SELECT
    DISTINCT department
FROM 
    employees


SELECT 
    DISTINCT ON (first_name) first_name, last_name
FROM 
    employees

--02C. Where
SELECT 
    first_name,
    last_name,
    salary
FROM employees
WHERE department = 'Human Resources' -- salary > 4500
ORDER BY salary DESC

--03. Multiple filters 
SELECT 
    e.id,
    e.first_name,
    e.last_name,
    e.job_title,
    e.department_id,
    e.salary
FROM
    employees as e
WHERE
    e.department_id = 4 AND e.salary >= 1000

--03. Multiple example
SELECT
    first_name,
    department,
    salary
FROM employees
WHERE (department = 'Sales' OR department = 'Marketing') AND salary >= 1000
ORDER BY department
-- WHERE salary BETWEEN 5000 AND 7000
-- WHERE salary IN (2100, 2200, 3000)
-- WHERE last_name IS NULL
-- WHERE last_name IS NOT NULL

--04. Data Manipulation
INSERT INTO towns VALUES (33, 'Paris')
--test all columns
INSERT INTO employees
VALUES (
    1001,
    'Petar',
    'Ivanov',
    'From the roof',
    'karlson@roof.com',
    'Male'
    9999,
    25,
    'Marketing'
)
--test some columns
INSERT INTO employees (id, first_name, last_name, gender, email, age, salary)
VALUES (
    1002,
    'Petar',
    'Ivanov',
    'Male'
    'karlson@roof.com',
    25,
    9999
)

--04. Insert into employees
INSERT INTO employees (first_name, last_name, job_title, department_id, salary)
VALUES 
    ('Samantha', 'Young', 'Housekeeping', 4, 900),
    ('Roger', 'Palmer', 'Waiter', 3, 928.33);
SELECT * FROM employees;

--create table from other records
CREATE TABLE customer_data
AS SELECT id, last_name, room_id
FROM clients;

--write to existing table
INSERT INTO projects(name, start_date)
SELECT name concat(name, ' ', 'Restructuring'), '2023-01-01'
FROM clients;

--05. Update
UPDATE employees
SET salary = 200 -- salary * 1.2
WHERE department = 'Human Resources';

--05. Update Task
UPDATE employees
SET salary = salary + 100
WHERE job_title = 'Manager';
SELECT * FROM employees
WHERE job_title = 'Manager';

--06. Delete
DELETE FROM employees
WHERE department = 'Legal'
--WHERE salary > 5000 or department = 'Shop'

SELECT count(*) FROM employees --shows number of records

--06. Delete Task
DELETE FROM employees
WHERE department_id = 1 OR department_id = 2;
--WHERE department_id IN (1, 2)
--WHERE department_id BETWEEN (1, 2)
SELECT * FROM employees
ORDER BY id;

--07. View
CREATE VIEW names_salary_set AS 
SELECT 
    first_name,
    last_name,
    salary
FROM employees;

SELECT first_name, salary FROM names_salary_set;

--7. View Task
CREATE VIEW best_paid AS
SELECT * FROM employees
ORDER BY salary DESC
LIMIT 1;
SELECT * FROM best_paid;

