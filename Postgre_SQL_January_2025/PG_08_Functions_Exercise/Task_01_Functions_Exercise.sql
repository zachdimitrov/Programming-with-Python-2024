-- 01. River Info
CREATE VIEW view_river_info AS
SELECT 
    CONCAT(
        'The river',
        ' ',
        river_name,
        ' ',
        'flows into the',
        ' ',
        outflow,
        ' ',
        'and is',
        ' ',
        "length",
        ' ',
        'kilometers long.'
        ) AS "River Information"
FROM rivers 
ORDER BY river_name;

SELECT * FROM view_river_info

-- 02. Geography Data
CREATE VIEW view_continents_countries_currencies_details AS
SELECT 
    CONCAT(c.continent_name, ': ', c.continent_code) 
    AS contitnet_details,
    CONCAT(co.country_name, ' - ', co.capital, ' - ', co.area_in_sq_km, ' - ', 'km2') 
    AS country_information,
    CONCAT(cu.description, ' ', '(', cu.currency_code,')') 
    AS currencies
FROM continents AS c, countries AS co, currencies AS cu
WHERE c.continent_code = co.continent_code AND co.currency_code = cu.currency_code
ORDER BY country_information, currencies;

SELECT * FROM view_continents_countries_currencies_details

-- 03. Capital Code
ALTER TABLE countries
ADD COLUMN capital_code CHAR(2);

UPDATE countries SET capital_code = LEFT(capital, 2)

-- 04. (Descr)iption
SELECT 
    SUBSTRING(description FROM 5) 
    -- RIGHT(description, -4)
FROM currencies

-- 05. Substring River Length
SELECT
-- 	(REGEXP_MATCHES("River Information", '([0-9]{1,4})'))[1] AS river_length
    SUBSTRING("River Information", '[0-9]{1,4}') AS river_length
FROM view_river_info

-- 06. Replace A
SELECT
    REPLACE(mountain_range, 'a', '@') AS replace_a,
    REPLACE(mountain_range, 'A', '$') AS "replace_A"
FROM mountains;

-- 07. Translate
SELECT
    capital, 
    TRANSLATE(capital, 'áãåçéíñóú', 'aaaceinou') AS translated_name
FROM countries;

-- 08. Leading
SELECT 
    continent_name,
    TRIM(LEADING FROM continent_name) AS trim
FROM continents;

-- 09. Trailing
SELECT 
    continent_name,
    TRIM(TRAILING FROM continent_name) AS trim
FROM continents;

-- 10. Left Right Trim
SELECT
    TRIM(LEADING 'Mm' FROM peak_name) AS left_trim,
    TRIM(TRAILING 'Mm' FROM peak_name) AS right_trim
FROM peaks

-- 11. Char lengths and bits
SELECT 
    CONCAT(m.mountain_range, ' ', p.peak_name) AS mountain_information,
    LENGTH(CONCAT(m.mountain_range, ' ', p.peak_name)) as characters_length,
    BIT_LENGTH(CONCAT(m.mountain_range, ' ', p.peak_name)) as bits_of_a_tring
FROM mountains AS m, peaks AS p
WHERE m.id = p.mountain_id;

-- 12. Length Number
SELECT
    population,
    LENGTH(CAST(population AS varchar))
FROM countries

-- 13. Positive Negative Left
SELECT
    peak_name,
    LEFT(peak_name, 4) AS positive_left,
    LEFT(peak_name, -4) as negative_left,
FROM peaks

-- 14. Positive Negative Right
SELECT
    peak_name,
    RIGHT(peak_name, 4) AS positive_right,
    RIGHT(peak_name, -4) as negative_right
FROM peaks

-- 15. Update iso_code
UPDATE countries
SET iso_code = UPPER(SUBSTRING(country_name, 1, 3))
WHERE iso_code IS NULL

SELECT id, iso_code FROM countries

-- 16. Reverse Country Code
UPDATE countries
SET country_code = LOWER(REVERSE(country_code));

SELECT id, country_code FROM countries ORDER BY id

-- 17. Elevation --->> Peak Name
SELECT 
    CONCAT_WS(' ', elevation, REPEAT('-', 3) || REPEAT('>', 2), peak_name) AS "Elevation --->> Peak Name"
FROM peaks
WHERE elevation >= 4884

-- 18. Arithmetical
CREATE TABLE booking_calculation
AS SELECT booked_for
FROM bookings
WHERE apartment_id = 93;

ALTER TABLE booking_calculation
ADD COLUMN multiplication NUMERIC, 
ADD COLUMN modulo NUMERIC;

UPDATE booking_calculation
SET multiplication = CAST(booked_for * 50 AS NUMERIC),
    modulo = CAST(booked_for % 50 AS NUMERIC);

/*
CREATE TABLE bookings_calculation
AS SELECT
	booked_for,
	CAST(booked_for * 50 AS NUMERIC) AS multiplication,
	CAST(booked_for % 50 AS NUMERIC) AS modulo
FROM bookings
WHERE apartment_id = 93;
*/

-- 19. Round vs Trunc
SELECT 
    latitude,
    ROUND(latitude, 2) AS round, 
    TRUNC(latitude, 2) AS trunc
FROM apartments

-- 20. Absolute Value
SELECT 
    longitude,
    ABS(longitude) AS abs
FROM apartments

-- 21. Billing Day
ALTER TABLE bookings
ADD COLUMN billing_day TIMESTAMPTZ;

UPDATE bookings
SET billing_day = CURRENT_TIMESTAMP;

SELECT 
    to_char(billing_day, 'DD "Day" MM "Month" YYYY "Year" HH24:MI:SS') AS "Billing DAY"
FROM bookings;

-- 22. Extract Booked At
SELECT
    EXTRACT(year FROM booked_at) AS "YEAR",
    EXTRACT(month FROM booked_at) AS "MONTH",
    EXTRACT(day FROM booked_at) AS "DAY",
    EXTRACT(hour FROM booked_at) AS "HOUR",
    EXTRACT(minute FROM booked_at) AS "MINUTE",
    EXTRACT(second FROM booked_at) AS "SECOND",
FROM bookings

-- 23. Early Birds
SELECT 
    id,
    AGE(booked_at, starts_at) AS early_birds
FROM bookings
WHERE starts_at - booked_at >= '10 months'

-- 24. Match or not
SELECT 
    companion_full_name,
    email
FROM users
WHERE companion_full_name ILIKE '%and%' AND email NOT LIKE '%@gmail'

-- 25. Count By Initial
SELECT 
    SUBSTRING(first_name, 1, 2) AS initials,
    COUNT('initials') AS user_count
FROM users
GROUP BY initials
ORDER BY user_count DESC, initials

-- 26. SUM
SELECT 
    SUM(booked_for) AS total_value
FROM bookings
WHERE apartment_id = 90