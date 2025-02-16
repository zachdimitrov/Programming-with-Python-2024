-- Task 1

CREATE TABLE owners(
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    phone_number VARCHAR(50) NOT NULL,
    address VARCHAR(50)
);

CREATE TABLE animal_types(
    id SERIAL PRIMARY KEY,
    animal_type VARCHAR(30) NOT NULL
);

CREATE TABLE cages(
    id SERIAL PRIMARY KEY,
    animal_type_id INT 
    REFERENCES animal_types 
    ON DELETE CASCADE
    ON UPDATE CASCADE
    NOT NULL
);

CREATE TABLE animals(
    id SERIAL PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    birthdate DATE NOT NULL,
    owner_id INT 
    REFERENCES owners 
    ON DELETE CASCADE
    ON UPDATE CASCADE,
    animal_type_id INT 
    REFERENCES animal_types
    ON DELETE CASCADE
    ON UPDATE CASCADE
    NOT NULL
);

CREATE TABLE volunteers_departments(
    id SERIAL PRIMARY KEY,
    department_name VARCHAR(30) NOT NULL
);

CREATE TABLE volunteers(
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    phone_number VARCHAR(15) NOT NULL,
    address VARCHAR(50),
    animal_id INT 
    REFERENCES animals
    ON DELETE CASCADE
    ON UPDATE CASCADE,
    department_id INT
    REFERENCES volunteers_departments
    ON DELETE CASCADE
    ON UPDATE CASCADE
    NOT NULL
);

CREATE TABLE animals_cages(
    cage_id INT
    REFERENCES cages
    ON DELETE CASCADE
    ON UPDATE CASCADE
    NOT NULL,
    animal_id INT
    REFERENCES animals
    ON DELETE CASCADE
    ON UPDATE CASCADE
    NOT NULL
);

-- Task 2

INSERT INTO volunteers(name, phone_number, address, animal_id, department_id)
VALUES
    ('Anita Kostova', '0896365412',	'Sofia, 5 Rosa str.', 15, 1),
    ('Dimitur Stoev', '0877564223',	NULL, 42, 4),
    ('Kalina Evtimova', '0896321112',	'Silistra, 21 Breza str.', 9, 7),
    ('Stoyan Tomov', '0898564100', 'Montana, 1 Bor str.', 18, 8),
    ('Boryana Mileva', '0888112233', NULL, 31, 5);

INSERT INTO animals(name, birthdate, owner_id, animal_type_id)
VALUES
    ('Giraffe',	'2018-09-21', 21, 1),
    ('Harpy Eagle',	'2015-04-17', 15, 3),
    ('Hamadryas Baboon', '2017-11-02', NULL, 1),
    ('Tuatara',	'2021-06-30', 2, 4);

-- Task 3

UPDATE animals
SET owner_id = (select id FROM owners AS o WHERE o.name = 'Kaloqn Stoqnov')
WHERE owner_id IS NULL;

-- Task 4

DELETE from volunteers_departments
WHERE department_name = 'Education program assistant';

-- Task 5

SELECT 
    name, 
    phone_number, 
    address,
    animal_id, 
    department_id
FROM volunteers
ORDER BY name ASC, animal_id ASC, department_id ASC;

-- Task 6

SELECT 
    a.name,
    t.animal_type,
    TO_CHAR(a.birthdate, 'DD.MM.YYYY') AS birthdate
FROM animals AS a
    JOIN animal_types AS t ON a.animal_type_id = t.id
ORDER BY a.name ASC;

-- Task 7

SELECT 
    o.name AS owner,
    count(*) AS count_of_animals
FROM owners AS o    
    JOIN animals AS a ON a.owner_id = o.id
GROUP BY o.name
ORDER BY count_of_animals DESC, owner ASC
LIMIT 5;

-- Task 8

SELECT
    concat(o.name, ' - ', a.name),
    o.phone_number,
    ac.cage_id
FROM owners AS o
    JOIN animals as a ON a.owner_id = o.id
        JOIN animals_cages AS ac ON ac.animal_id = a.id
            JOIN animal_types AS at ON at.id = a.animal_type_id
WHERE at.animal_type = 'Mammals'
ORDER BY o.name, a.name DESC;

-- Task 9

SELECT
    v.name AS volunteers,
    v.phone_number,
    -- TRIM(v.address, 'Sofia, ')
    TRIM(REPLACE(REPLACE(v.address, 'Sofia', ''), ',', '')) AS address
FROM volunteers AS v
    JOIN volunteers_departments AS vd ON v.department_id = vd.id
WHERE vd.department_name = 'Education program assistant'
    AND v.address LIKE '%Sofia%'
ORDER BY v.name ASC;

-- Task 10

SELECT 
    a.name AS animal,
    EXTRACT(YEAR FROM a.birthdate) AS birth_year,
    at.animal_type
FROM animals AS a   
    JOIN animal_types as at ON a.animal_type_id = at.id
WHERE at.animal_type <> 'Birds' 
    AND AGE('01/01/2022', a.birthdate) < '5 year'
    AND a.owner_id IS NULL
ORDER BY a.name ASC;

-- Task 11

CREATE OR REPLACE FUNCTION fn_get_volunteers_count_from_department(searched_volunteers_department VARCHAR(30))
RETURNS INT
AS
$$
    DECLARE volunteers INT;
    BEGIN
        volunteers := 
        (
            SELECT 
                count(*)
            FROM volunteers AS v
                JOIN volunteers_departments AS vd ON v.department_id = vd.id
            WHERE vd.department_name = searched_volunteers_department
        );
        RETURN volunteers;
    END
$$
LANGUAGE plpgsql;

SELECT 
    count(*)
FROM volunteers AS v
    JOIN volunteers_departments AS vd ON v.department_id = vd.id
WHERE vd.department_name = 'Zoo events'

-- Task 12

SELECT
    o.name
FROM owners AS o
    JOIN animals AS a ON o.id = a.owner_id
WHERE a.name = ''

CREATE OR REPLACE PROCEDURE sp_animals_with_owners_or_not(
    IN animal_name VARCHAR(30),
    OUT result VARCHAR(30)
    )
AS
$$
    BEGIN
        SELECT
            o.name
        FROM owners AS o
            JOIN animals AS a ON o.id = a.owner_id
        WHERE a.name = animal_name INTO result;
        IF
            result IS NULL THEN
            result := 'For adoption';
        END IF;
    END
$$
LANGUAGE plpgsql