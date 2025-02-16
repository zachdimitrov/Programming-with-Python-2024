/*
Database Design
---------------
1. Identify the entities
2. Define Table Columns
3. Define Primary Keys
4. Modeling Relationships
5. Defining Constrains - use NOT NULL 
6. Filling Test Data

Table design principles:

1. Без повторения на данни. 
2. Уникални идентификатори.
3. NULL само на места, където е необходимо.
4. Интеграция на референциите
5. Atomic data - данните са разбити на малки части. 
    Пазим first_name and last_name отделно за да можем да ги достъпим отделно.
6. Подбор на правилни данни
7. Индексация
8. Access control

Primary Key
-----------
1. Not existing column
2. Integer is best
3. First column
4. Exceptions - not preferable

Relationships
-------------
PRIMARY KEY / FOREIGN KEY
id          / city_id
city        / persons

1. One-to-many - mountain / peaks
2. Many-to-many - 
3. One-to -one - 

PRIMARY KEY
-----------
id INT PRIMARY KEY
id SERIAL PRIMARY KEY
id INT GENERATED ALWAYS AS IDENTITY
id INT GENERATED DEFAULT AS IDENTITY

*/

-- create relation
ALTER TABLE persons
ADD CONSTRAINT fk_country 
FOREIGN KEY (country_id) 
REFERENCES countries(id)

SELECT * FROM 
persons AS p 
JOIN 
countries AS c
ON p.country_id = c.id

-- create primary key
CREATE TABLE countries(
    id SERIAL PRIMARY KEY,
    name VARCHAR(20)
);

CREATE TABLE people(
    id SERIAL PRIMARY KEY,
    name VARCHAR(20),
    country_id int REFERENCES countries
);

INSERT INTO countries (name)
VALUES 
	('Bulgaria'), 
	('France'), 
	('Germany'), 
	('Greece'), 
	('Portugal'), 
	('Sweden');


INSERT INTO people (name, country_id)
VALUES
    ('Ivan', 1),
    ('Gosho', 2),
    ('Pesho', 3),
    ('Petko', 4),
    ('Todor', 5),
    ('Ivo', 6),
    ('Stoyan', 1),
    ('Yasen', 2),
    ('Toni', 3),
    ('Jivko', 4),
    ('Koko', 5),
    ('Momchil', 6);

INSERT INTO people (name, country_id)
VALUES
    ('Glavan', (SELECT id FROM countries WHERE country = 'France')),
    ('Tosho', (SELECT id FROM countries WHERE country = 'France')),
    ('Kamen', (SELECT id FROM countries WHERE country = 'Portugal')),
    ('Ivan', (SELECT id FROM countries WHERE country = 'Greece'));

select p.name, c.name  FROM people as p
JOIN countries as c
ON p.country_id = c.id

-- Task 1. Mountains Peaks
CREATE TABLE mountains(
    id SERIAL PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE peaks(
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    mountain_id INT,
    CONSTRAINT fk_peaks_mountains FOREIGN KEY (mountain_id) REFERENCES mountains(id)
);

/*
Many to many
------------
1. Junction table - can add more columns
2. Composite Key - two foreign keys
*/

CREATE TABLE men(
    id SERIAL PRIMARY KEY,
    name VARCHAR(20)
);

CREATE TABLE women(
    id SERIAL PRIMARY KEY,
    name VARCHAR(20)
);

CREATE TABLE men_women(
    men_id INT REFERENCES men(id),
    women_id INT REFERENCES women(id),
    CONSTRAINT pk_men_women PRIMARY KEY (men_id, women_id)
);

INSERT INTO men(name)
VALUES 
    ('Ivan'),
    ('Gosho'),
    ('Pesho'),
    ('Joro'),
    ('Kancho');

INSERT INTO women(name)
VALUES 
    ('Iana'),
    ('Penka'),
    ('Ganka'),
    ('Tonka'),
    ('Kunka');

INSERT INTO men_women
VALUES
    (1, 2),
    (1, 3),
    (1, 4),
    (2, 2),
    (2, 3),
    (3, 1),
    (4, 2);

SELECT
    m.name,
	w.name
FROM men AS m
	JOIN men_women AS mw ON m.id = mw.men_id
		JOIN women AS w ON mw.women_id = w.id

-- Long Syntax
CREATE TABLE employees(
    id SERIAL PRIMARY KEY,
    employee_name VARCHAR(50)
);

CREATE TABLE projects(
    id SERIAL PRIMARY KEY,
    project_name VARCHAR(50)
);

CREATE TABLE employees_projects (
    employee_id INT,
    project_id INT,
    
    CONSTRAINT pk_employees_projects
    PRIMARY KEY (employee_id, project_id),

    CONSTRAINT fk_employees_projects_employees
    FOREIGN KEY (employee_id)
    REFERENCES employees(id),

    CONSTRAINT fk_employees_projects_projects
    FOREIGN KEY (project_id)
    REFERENCES projects(id)
);

/*
-- One to one
-------------
-- Rarely used - for different modules
-- Avoid NULL values

table 1        table 2
name1    ->    profile1
name2    ->    profile2
name3
name4
*/

CREATE TABLE capitals(
    capital_id SERIAL PRIMARY KEY,
    capital_name VARCHAR(50)
);

CREATE TABLE countries(
    country_id SERIAL PRIMARY KEY,
    capital_id INT UNIQUE,
    CONSTRAINT fk_countries_capitals 
    FOREIGN KEY (capital_id) REFERENCES capitals(capital_id)
);

-- Join
SELECT
    p.first_name,
    p.last_name,
    c.country
FROM persons AS p
    JOIN countries AS c ON p.country_id = c.id

-- Task 2
SELECT
    v.driver_id,
    v.vehicle_type,
    concat(c.first_name, ' ', c.last_name) as driver_name
FROM vehicles as v
    join campers as c on c.id - v.driver_id

-- Task 3
SELECT
    r.start_point,
    r.end_point,
    r.leader_id,
    concat(c.first_name, ' ', c.last_name) as leader_name
FROM routes AS r
    JOIN campers AS c ON r.leader_id = c.id

/*
Cascade operations
------------------
Deleting parent - deletes all children
*/

ALTER TABLE persons
DROP CONSTRAINT fk_country,
ADD CONSTRAINT fk_country FOREIGN KEY (country_id)
    REFERENCES countries(id) 
    ON DELETE CASCADE 
    ON UPDATE CASCADE;
 -- ON DELETE SET NULL -- sets deleted as NULL
 -- ON DELETE RESTRICT -- does not let deletion
 -- ON DELETE NO ACTION -- does not let to delete but after the full transacrion

DELETE FROM countries
WHERE id = 2;

UPDATE countries
SET id = 22
WHERE id = 1

-- Task 4.
CREATE TABLE mountains(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE peaks(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(50),
    mountain_id INT,
    CONSTRAINT fk_mountain_id
        FOREIGN KEY (mountain_id)
            REFERENCES mountains(id)
                ON DELETE CASCADE
);