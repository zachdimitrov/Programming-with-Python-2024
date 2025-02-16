-- Functions
-- first_name + last_name -> initials
CREATE OR REPLACE FUNCTION fn_names_to_initials(varchar, varchar)
RETURNS varchar(5) AS 
$$
    BEGIN
        RETURN concat(left($1, 1), '.', left($2, 1), '.');
    END
$$
LANGUAGE plpgsql

SELECT fn_names_to_initials('Zahari', 'Dimitrov');

-- Declare Variables
CREATE OR REPLACE FUNCTION fn_names_to_initials(varchar, varchar)
RETURNS varchar(5) AS 
$$
    DECLARE
        first_name ALIAS FOR $1; 
        first_name ALIAS FOR $2; 
    BEGIN
        RETURN concat(left(first_name, 1), '.', left(last_name, 1), '.');
    END
$$
LANGUAGE plpgsql


-- Declare Variables second option
CREATE OR REPLACE FUNCTION fn_names_to_initials(first_name varchar, last_name varchar)
RETURNS varchar(5) AS 
$$
    BEGIN
        RETURN concat(left(first_name, 1), '.', left(last_name, 1), '.');
    END
$$
LANGUAGE plpgsql

DROP FUNCTION fn_names_to_initials

-- full name
CREATE OR REPLACE FUNCTION fn_get_full_name(first_name varchar, last_name varchar)
RETURNS varchar AS
$$
    DECLARE
        full_name varchar;
    BEGIN
        IF first_name IS NULL AND last_name IS NULL THEN
            full_name := 'No Name'L;
        ELSIF first_name is NULL THEN 
            full_name := last_name;
        ELSIF last_name IS NULL THEN
            full_name := first_name;
        ELSE full_name := concat(first_name, ' ', last_name);
        END IF;
        RETURN full_name;
    END
$$
LANGUAGE plpgsql

SELECT fn_get_full_name('Zahari', 'Dimitrov')

-- work with tables
CREATE OR REPLACE FUNCTION fn_get_country_id(c varchar)
RETURNS INT AS
$$
    DECLARE 
        country_id INT;
    BEGIN
        SELECT id FROM countries WHERE country = c INTO country_id;
        RETURN country_id;
    END
$$
LANGUAGE plpgsql;

-- Таск 01.
CREATE OR REPLACE FUNCTION fn_count_employees_by_town(town_name varchar(20))
RETURNS INT AS
$$
    DECLARE 
        employee_count INT;
    BEGIN
        SELECT count(e) FROM employees AS e JOIN addresses AS a USING(address_id)
            JOIN towns AS t USING(town_id)
        WHERE t.name = town_name INTO employee_count;
        RETURN employee_count;
    END
$$
LANGUAGE plpgsql;

-- no return
CREATE OR REPLACE FUNCTION fn_add_country(c_name varchar, c_id int)
RETURNS BOOL AS
$$
    BEGIN
        INSERT INTO countries(id, country)
        VALUES (s_id, c_name);
        RETURN TRUE;
        EXCEPTION
            WHEN UNIQUE_VIOLATION THEN RETURN FALSE; -- if id is already used
    END
$$
LANGUAGE plpgsql;

SELECT fn_add_country('Norway', 44)

-- return table
CREATE OR REPLACE FUNCTION fn_get_persons()
RETURNS TABLE(id INT, full_name VARCHAR, country_name VARCHAR) AS
$$
    BEGIN
        RETURN QUERY (
            SELECT
                p.id,
                concat(p.first_name, ' ', p.last_name)::varchar AS full_name.
                c.country_name
            FROM persons AS p JOIN countrites AS c ON p.country_id = c.id
        );
    END
$$
LANGUAGE plpgsql;

select * FROM fn_get_persons();

-- other
CREATE OR REPLACE FUNCTION fn_get_persons()
RETURNS TABLE(id INT, full_name VARCHAR, country_name VARCHAR) AS
$$
    BEGIN
        RETURN QUERY (
            SELECT 
				p.id, 
				p.name AS full_name, 
				c.name AS country_name 
			FROM people AS p 
				JOIN countries AS c 
					ON p.country_id = c.id
        );
    END
$$
LANGUAGE plpgsql;

select * FROM fn_get_persons();

-- debugging
CREATE OR REPLACE FUNCTION fn_show_message(msg varchar)
RETURNS BOOL AS
$$
    BEGIN
        RAISE NOTICE 'Very important notice: %', msg;
    END
$$
LANGUAGE plpgsql;


/*
Stored procedures
same as function but no return
*/

CREATE OR REPLACE PROCEDURE sp_increase_salaries(department_name varchar)
AS 
$$
    BEGIN
        UPDATE employees
        SET salary = salary * 1.05
        WHERE department_id = 
        (SELECT department_id FROM departments WHERE name = department_name);
    END
$$
LANGUAGE plpgsql;

-- add country with erron message
CREATE OR REPLACE PROCEDURE sp_add_country(
    IN c_name varchar,
    IN c_id int,
    OUT status int,
    OUT msg varchar
)
AS 
$$
    BEGIN
        INSERT INTO countries(id, name)
        VALUES (s_id, c_name);
        status := 0;
        EXCEPTION
            WHEN UNIQUE_VIOLATION THEN status := 1;
            msg := SQLERRM;
            RAISE NOTICE 'error %', SQLERRM;
    END
$$
LANGUAGE plpgsql;

CALL sp_add_country('Bolivia', 51, 0, '')

-- Transactions
CEREATE TABLE bank(
    id int PRIMARY KEY,
    name VARCHAR,
    bgn INT
);

INSERT INTO bank(id, name, bgn)
VALUES
    (1, 'Ivan', 1000),
    (2, 'Mimi', 2000),
    (3, 'Gosho', 3000);

CREATE OR REPLACE PROCEDURE sp_transfer_money(
    IN sender_id int,
    IN receiver_id int,
    IN transfer_amount int,
    OUT status varchar(50)
)
AS
$$
    DECLARE
        sender_amount int;
        receiver_amount int;
        temp_val int;
    BEGIN
        SELECT bgn FROM bank WHERE id = sender_id INTO sender_amount;
        IF sender_amount < transfer_amount THEN
            status := 'The sender does not have enough money';
            RETURN;
        END IF;
        SELECT bgn FROM bank WHERE id = receiver_id INTO receiver_amount;
        UPDATE bank SET bgn = bgn + transfer_amount WHERE id = receiver_id;
        UPDATE bank SET bgn = bgn - transfer_amount WHERE id = sender_id;
        SELECT bgn FROM bank WHERE id = sender_id INTo temp_val;
        IF sender_amount - transfer_amount <> temp_val THEN
            status := 'Error transfer from sender';
            ROLLBACK;
            RETURN;
        END IF;
        SELECT bgn FROM bank WHERE id = receiver_id INTO temp_val;
        IF receiver_amount + transfer_amount <> temp_val THEN
            status := 'Error in receiver';
            ROLLBACK;
            RETURN;
        END IF;
        status := 'Success';
        COMMIT;
    END
$$
LANGUAGE plpgsql;

CALL sp_transfer_money(1, 2, 300, '')

/*
SAVEPOINT;

*/

-- Task 03.
CREATE OR REPLACE PROCEDURE sp_increase_salary_by_id(id INT)
AS
$$
    BEGIN
        IF (SELECT employee_id FROM employees WHERE employee_id = id) IS NULL THEN
            RETURN;
        END IF;
        UPDATE employees SET salary = salary * 1.05 WHERE employee_id = id;
        COMMIT;
    END
$$
LANGUAGE plpgsql;

CALL sp_increase_salary_by_id(5);

-- Triggers
CREATE TABLE items(
    id INT PRIMARY KEY,
    status INT
);

CREATE TABLE items_log(
    id INT PRIMARY KEY,
    status INT, 
    created date DEFAULT now()
);

-- Triggers
DROP FUNCTION log_items CASCADE;

CREATE FUNCTION log_items()
RETURNS TRIGGER AS 
$$
    BEGIN  
        INSERT INTO items_log(id, status)
        VALUES (new.id, new.status);
        RETURN new;
    END
$$
LANGUAGE plpgsql;

DROP TRIGGER log_items_trigger;

CREATE TRIGGER log_items_trigger
AFTER INSERT ON items
FOR EACH ROW EXECUTE PROCEDURE log_items();

INSERT INTO items (id, status)
VALUES 
    (1, floor(random()*100)),
    (2, floor(random()*100)),
    (3, floor(random()*100)),
    (4, floor(random()*100)),
    (5, floor(random()*100)),
    (6, floor(random()*100));

------ leave only last 8 in log

CREATE OR REPLACE FUNCTION delete_last_items_log()
RETURNS TRIGGER
AS 
$$
    BEGIN
        WHILE (SELECT count(*) FROM items_log) > 8 LOOP
            DELETE FROM items_log WHERE id = (SELECT min(id) FROM items_log);
        END LOOP;
        RETURN new;
    END
$$
LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER clear_items_log_trigger
    AFTER INSERT ON items_log
FOR EACH STATEMENT EXECUTE PROCEDURE delete_last_items_log();


