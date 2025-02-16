-- concatenation
SELECT CONCAT(first_name, ' ', last_name) AS full_name
FROM authors;

SELECT CONCAT_WS(', ', last_name, born, other) AS summary
FROM authors;

-- string manipulation
SELECT SUBSTRING(description, 1, 50) AS summary
FROM books;

SELECT SUBSTRING(first_name FROM 1 FOR 1) AS first_initial
FROM authors;

--01 Find The Book
SELECT title FROM books
WHERE SUBSTRING(title, 1, 3) = 'The'
ORDER BY id;

-- characters from side
SELECT LEFT(title, 10) AS short_title
FROM books;

-- RIGHT(string, count)

-- replacing strings
SELECT REPLACE(title, 'Murder', '******') AS title_censored
FROM books;

--02 Replace Title
SELECT REPLACE(title, 'The', '***') as "Title"
FROM books
WHERE SUBSTRING(title, 1, 3) = 'The'
ORDER BY id;

-- other functions
/*
-- remove from both sides
SELECT TRIM(string)
SELECT TRIM(BOTH ' ' FROM '   Uni   ')

-- remove from left
SELECT TRIM(LEADING FROM string)

-- remove from right
SELECT TRIM(TRAILING FROM string)

-- change casing
LOWER(string)
UPPER(string)
REVERSE(string)
REPEAT(string, count)
LENGTH(string)
CHAR_LENGTH(string)
BIT_LENGTH(string)

-- more string functions here
https://www.postgresql.org/docs/9.1/functions-string.html
*/

-- math functions
SELECT id,
    (side*height)/2 AS area
FROM triangles
ORDER BY id;

/*
- - Subtraction
+ - Addition
* - Multiplication
/ - Division
%, MOD(a, b) - Modulo
^, POWER(a, b) - Exponentiation
|/, SQRT(a) - Square root
@, ABS(a) - Absolute value

SELECT PI(); -- 3.14159...
SELECT DIV(11, 2); -- 5 - integer division

SELECT FLOOR(33.68); -- 33 
SELECT CEILING(33.68); -- 34

SELECT ROUND(33.68888); -- 34
SELECT ROUND(33.68888, 2) -- 33.69
SELECT ROUND(33.68888, -1) -- 30

SELECT TRUNC(12.588); -- 12
SELECT TRUNC(12.588, 1); -- 12.5
*/

--03 Format Costs
SELECT title,
    TRUNC(cost, 3)
AS modified_price
FROM books
ORDER BY id;

-- date time functions

/*
EXTRACT(part FROM date)
AGE(first_date, second_date)
NOW(); -- 2025-01-27 10:46:53.234562+02
CURRENT_DATE; -- 2025-01-27
CURRENT_TIME; -- 10:46:53.234562+02
TO_CHAR(NOW(), 'DD Month YYYY') -- 23 Janyary 2025
*/

-- how long they lived
SELECT 
    CONCAT(first_name, ' ', last_name) AS "Full Name",
    AGE(died, born) AS "Life Span"
FROM authors;

-- year of birth
SELECT
    first_name,
    last_name,
    EXTRACT(year FROM born) AS year
FROM authors;

-- format date of birth
SELECT
    last_name AS "Last Name",
    TO_CHAR(born, 'DD (Dy) Mon YYYY') AS "Date of Birth"
FROM authors;

-- wild cards
/*
'%' -- zero, one or many characters
'_' -- a single character

WHERE last_name LIKE 'S%'; -- starts with 'S'
WHERE middle_name LIKE '_o%'; -- second letter is 'o'
WHERE first_name LIKE 'A%a'; -- starts with 'A' and ends with 'a'
*/

SELECT id, last_name
FROM authors
WHERE last_name LIKE '%l!_%' ESCAPE '!'; -- special character escape prefix

-- Select Harry Potter Books
SELECT title FROM books
WHERE title LIKE '%Harry Potter%'
ORDER BY id;