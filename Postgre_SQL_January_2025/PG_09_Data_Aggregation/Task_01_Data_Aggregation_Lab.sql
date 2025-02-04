SELECT  
    country,
    department,
    count(*)
FROM persons
GROUP BY country, department
ORGER BY country

-- 01. Departmetns
SELECT
    department_id,
    count(*) AS employee_count
FROM employees
GROUP BY department_id
ORDER BY department_id

-- 02. Departments Info
SELECT
    department_id,
    count(salary) AS employee_count
FROM employees
GROUP BY department_id
ORDER BY department_id

-- 03. Sum Salary
SELECT
    department_id,
    SUM(salary) AS total_salary
FROM employees
GROUP BY department_id
ORDER BY department_id

-- 04. Max salary
SELECT
    department_id,
    MAX(salary) AS max_salary
FROM employees
GROUP BY department_id
ORDER BY department_id

-- 05. Min salary
SELECT
    department_id,
    MIN(salary) AS min_salary
FROM employees
GROUP BY department_id
ORDER BY department_id

-- 06. Avg salary
SELECT
    department_id,
    AVG(salary) AS avg_salary
FROM employees
GROUP BY department_id
ORDER BY department_id
WHERE salary NOT NULL

-- 07. Filter Total Salaries
SELECT 
    department_id,
    SUM(salary) AS "Total Salary"
FROM employees
GROUP BY department_id
HAVING SUM(salary) <= 4100
ORDER BY "Total Salary" DESC

-- 08. Department Names
SELECT  
    id, 
    first_name,
    last_name,
    TRUNC(salary, 2),
    department_id,
    CASE
		WHEN department_id = 1 THEN 'Management'
        WHEN department_id = 2 THEN 'Kitchen Staff'
        WHEN department_id = 3 THEN 'Service Staff'
		ELSE 'Other'
	END AS department_name
FROM employees