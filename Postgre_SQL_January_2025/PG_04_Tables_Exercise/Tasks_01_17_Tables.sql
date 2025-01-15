-- 00. Create database
CREATE DATABASE IF NOT EXISTS "minions_db"

-- 01. Create a table
CREATE TABLE minions (
    id SERIAL PRIMARY KEY,
    -- id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(30),
    age INT
)

--02. Rename table
ALTER TABLE minions
RENAME TO minions_info;

--03. Alter table
ALTER TABLE minions_info
ADD COLUMN code CHAR(4),
ADD COLUMN task TEXT,
ADD COLUMN salary DECIMAL(8,3) DEFAULT 0;

--04. Rename Column
ALTER TABLE minions_info
RENAME COLUMN salary TO banana

--05. Add Columns
ALTER TABLE minions_info
ADD COLUMN email VARCHAR(20),
ADD COLUMN equipped BOOLEAN NOT NULL DEFAULT FALSE;

--06. Create ENUM
CREATE TYPE type_mood AS ENUM ('happy', 'relaxed', 'stressed', 'sad')
ALTER TABLE minions_info
ADD COLUMN mood type_mood;

--07. Set Default
ALTER TABLE minions_info
ALTER COLUMN age SET DEFAULT 0,
ALTER COLUMN name SET DEFAULT '',
ALTER COLUMN code SET DEFAULT '';

--08. Add Constraints
ALTER TABLE minions_info
ADD CONSTRAINT banana_check
CHECK (banana > 0),
ADD CONSTRAINT unique_constraint
UNIQUE (id, email);

--09. Change Column Data Type
ALTER TABLE minions_info
ALTER COLUMN task
TYPE VARChAR(150);

--10. Drop Constraint
ALTER TABLE minions_info
ALTER COLUMN equipped
DROP NOT NULL;

--11. Remove Column
ALTER TABLE minions_info
DROP age;

--12. Table Birthdays
CREATE TABLE minions_birthdays (
    id SERIAL PRIMARY KEY,
    -- id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(50),
    date_of_birth DATE,
    age INT, 
    present VARCHAR(100),
    party TIMESTAMPTZ
);

--13. Insert Data
INSERT INTO 
	minions_info(name, code, task, banana, email, equipped, mood)
VALUES 
	('Mark', 'GKYA', 'Graphing Points', 3265.265, 'mark@minion.com', false, 'happy'),
	('Mel', 'HSK', 'Science Investigation', 54784.996, 'mel@minion.com', true, 'stressed'),
	('Bob', 'HF', 'Painting', 35.652, 'bob@minion.com', true, 'happy'),
	('Darwin', 'EHND', 'Create a Digital Greeting', 321.958, 'darwin@minion.com', false, 'relaxed'),
	('Kevin', 'KMHD', 'Construct with Virtual Blocks', 35214.789, 'kevin@minion.com', false, 'happy'),
	('Norbert', 'FEWB', 'Testing', 3265.500, 'norbert@minion.com', true, 'sad'),
	('Donny', 'L', 'Make a Map', 8.452, 'donny@minion.com', true, 'happy');

--14. Select
SELECT
	name,
	task,
	email,
	banana
FROM 
	minions_info;

--15. Truncate Table
TRUNCATE TABLE minions_info;

--15. Drop Table
DROP TABLE minions_birthdays;

--16. Drop Database
DROP DATABASE minions_db WITH (FORCE);

--17. Bonus
CREATE TYPE address AS (
	street VARCHAR(50),
	city VARCHAR(50),
	postal_code CHAR(4)
);

CREATE TABLE customers (
	id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
	customer_name VARCHAR(100),
	customer_address address
);

INSERT INTO 
	customers(customer_name, customer_address)
VALUES
	('Pesho', ('ulitsa marica', 'sofia', '1600'));


SELECT 
	(customer_address).street,
	(customer_address).postal_code
FROM 
	customers;