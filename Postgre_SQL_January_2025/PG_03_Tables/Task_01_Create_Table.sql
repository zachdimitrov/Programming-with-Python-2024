CREATE DATABASE gamebar;
-- task 1
CREATE TABLE employees (
    id SERIAL PRIMARY KEY NOT NULL,
    first_name VARCHAR (30),
    last_name VARCHAR (50),
    hiring_date DATE DEFAULT '2023-01-01',
    salary NUMERIC(10, 2),
    devices_number INT
);
CREATE TABLE departments (
	id SERIAL PRIMARY KEY NOT NULL,
	name VARCHAR (50),
	code CHAR (3),
	description TEXT
);
CREATE TABLE issues (
	id SERIAL PRIMARY KEY NOT NULL,
	description VARCHAR (150), 
	date DATE,
	start TIMESTAMP
);

-- task 2
ALTER TABLE employees
ADD middle_name VARCHAR(50),

-- task 3
ALTER TABLE employees
ALTER COLUMN salary SET NOT NULL,
ALTER COLUMN salary SET DEFAULT 0,
ALTER COLUMN hiring_date SET NOT NULL

-- task 4
ALTER TABLE employees
ALTER COLUMN middle_name TYPE VARCHAR(100)

-- task 5
TRUNCATE TABLE issues

-- task 6
DROP TABLE departments