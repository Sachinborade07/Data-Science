-- CONDITIONAL EXPRESSION

SELECT * FROM customer

SELECT customer_id FROM customer

SELECT customer_id,
CASE 
	WHEN (customer_id < 100) THEN 'PREMIUM'
	WHEN (customer_id BETWEEN 100 AND 200) THEN 'PLUS'
	ELSE 'NORMAL' 
END 
FROM customer

--------------------------

--- Adding the ALIAS name
SELECT customer_id,
CASE 
	WHEN (customer_id < 100) THEN 'PREMIUM'
	WHEN (customer_id BETWEEN 100 AND 200) THEN 'PLUS'
	ELSE 'NORMAL' 
END AS customer_class
FROM customer

--------------------------

SELECT customer_id,
CASE customer_id 
		WHEN 2 THEN 'WINNER'
		WHEN 5 THEN 'SECOND PLACE'
		ELSE 'NORMAL'
END AS raffle_results
FROM customer

----------------------------------------------------------------------------

SELECT * FROM film

SELECT rental_rate FROM film

SELECT rental_rate,
CASE rental_rate
		WHEN 0.99 THEN 1
		WHEN 2.99 THEN 3
		WHEN 4.99 THEN 5
		ELSE 0
END AS rounded_off
FROM film

----- checking how many 0.99 are there
SELECT 
SUM( CASE rental_rate
	 WHEN 0.99 THEN 1
	 ELSE 0
END ) AS number_of_bargains
FROM film

