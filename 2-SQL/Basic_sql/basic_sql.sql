-- selecting from film*/
select * from film

-- looking into the actor table */
select * from actor

--looking in to some more table */
select * from city
  
-- to get only single column */
select first_name from actor

-- select two columns */
select first_name, last_name from actor 

-- changing the order of the statement */
select last_name, first_name from actor 


-- we have to send out a promotional email to our existing custor */
select first_name,last_name,email from customer



-- selecting from film  
select * from film


-- selecting distinct values using DISTINCT keyword 
select distinct release_year from film

-- or  
select distinct(release_year) from film

/* distinct rental_rate */
select distinct(rental_rate) from film

/* an australian visitor isn't familiar with MPAA movie rating
we want the type of rating 
*/

select distinct(rating) from film 


/* Using aggergate function  */ 
select count(category_id) from film_category

/* Getting the maximum amount from the payment  */ 

select max(amount) from payment


-- using the count function 
select count(*) from payment

select count(amount) from payment

select amount from payment

-- to remove duplicate payment
select distinct amount from payment 

select count(distinct amount) from payment


-- checking cutomer column	
select * from customer

select * from customer 
where first_name = 'Jared';

-- checking film column
select * from film

select * from film 
where rental_rate > 4;

select * from film
where rental_rate > 4 and replacement_cost >= 19.99

select rental_rate from film
where rental_rate > 4 and replacement_cost >= 19.99
and rating='R';

select title from film
where rental_rate > 4 and replacement_cost >= 19.99
and rating='R';
 
select * from film
where rental_rate > 4 and replacement_cost >= 19.99
and rating='R';

select count(title) from film
where rental_rate > 4 and replacement_cost >= 19.99
and rating='R';

select count(*) from film
where rental_rate > 4 and replacement_cost >= 19.99
and rating='R';

select count(*) from film
where rating='R' or rating='PG-13'

select * from film
where rating != 'R'


-- Nancy forget their wallet 
select email from customer 
where first_name ='Nancy';

-- a customer

select description from film 
where title = 'Outlaw Hanky'



-- How many female customers do we have from the state of Oregon (OR)
SELECT COUNT(first_name) 
FROM customer
WHERE gender='F' and state='OR';

-- who over the age of 44 has an income of 100000 or more( excluding 44)



-- 3/7/24

select * from customer
where first_name LIKE 'J%'
-- here pattern matching should be in 'single quotes'


-- starting with 'J'
SELECT COUNT(*) FROM customer
WHERE first_name LIKE 'J%'

-- starting with 'J' and ending with 'S'
SELECT COUNT(*) FROM customer
WHERE first_name LIKE 'J%' AND last_name LIKE 'S%'

-- JUST checking  " ILIKE " pattern matching 
SELECT * FROM customer
WHERE first_name ILIKE 'j%' AND last_name ILIKE 's%'


SELECT * FROM customer
WHERE first_name LIKE '%er%'

SELECT * FROM customer 
WHERE first_name LIKE '%her%'


-- starting from any letter followed by _her % means any character after "her".
SELECT * FROM customer 
WHERE first_name LIKE '_her%'


SELECT * FROM customer 
WHERE first_name NOT LIKE '_her%'

SELECT * FROM customer
WHERE first_name LIKE 'A%'
ORDER BY last_name


SELECT * FROM customer
WHERE first_name LIKE 'A%' AND last_name NOT LIKE 'B%'
ORDER BY last_name

-- Q) How many payment transaction were greater than $5.00
select count(*) from payment
where amount > 5;
-- OR 
SELECT COUNT(amount) FROM payment
WHERE amount > 5

-- How many actors have a first name that starts with the letter P
SELECT COUNT(*) FROM actor
WHERE first_name LIKE 'P%'


-- How many unique districts are our customers from 
SELECT COUNT(DISTINCT(district))
FROM address


-- How many films have a rating of R and a replacement cost between $5 and $15 
SELECT COUNT(*) FROM film
WHERE rating='R'
AND replacement_cost BETWEEN 5 AND 15;

SELECT * FROM film 

-- how many films have Truman in its name 
SELECT COUNT(*) FROM film 
WHERE title LIKE '%Truman%'


------------------------------------------------------------------
-- Trying all the aggregate functions

SELECT MIN(replacement_cost) FROM film 

SELECT MAX(replacement_cost) FROM film 

SELECT MAX(replacement_cost), MIN(replacement_cost)
FROM film


--
-- 5/7/24

SELECT * FROM payment

SELECT customer_id,staff_id,SUM(amount) FROM payment
GROUP BY staff_id, customer_id

SELECT staff_id,customer_id,SUM(amount) FROM payment
GROUP BY staff_id, customer_id


SELECT staff_id,customer_id,SUM(amount) FROM payment
GROUP BY staff_id, customer_id
ORDER BY staff_id
-- we can see the change in the order of staff_id 
-- based on staff_id all the changes are getting done .


SELECT staff_id,customer_id,SUM(amount) FROM payment
GROUP BY staff_id, customer_id
ORDER BY staff_id,customer_id
-- now the output is getting ORDER_BY both staff_id and customer_id 

SELECT staff_id,customer_id,SUM(amount) FROM payment
GROUP BY staff_id, customer_id
ORDER BY SUM(amount)



SELECT * FROM PAYMENT

SELECT DATE(payment_date) FROM payment
-- Here the date is getting only extracted 

SELECT DATE(payment_date) FROM payment
GROUP BY DATE(payment_date)
-- now the dates are in the arranged format

SELECT DATE(payment_date) FROM payment
GROUP BY DATE(payment_date)
ORDER BY SUM(amount)
-- here we are ordering by the SUM(amount)


-- still the result is not good 
-- so use DESC function 
SELECT DATE(payment_date) FROM payment
GROUP BY DATE(payment_date)
ORDER BY SUM(amount) DESC

-- WE WANT TO GIVE BONUS TO staff_id 1 & 2 which having highest number of engagement
SELECT * FROM PAYMENT

SELECT staff_id,COUNT(amount) 
FROM payment 
GROUP BY (staff_id )
-- now we can see staff_id 2 will get the bonus as highest number of engagement with customers 


-- Corporate HQ is conducting a study on the relationship between replacement cost and movie MPAA rating
-- what is the average replacement cost per MPAA rating 
-- NOTE: You may need to expand the AVG column to view correct results .

SELECT * FROM film 

SELECT AVG(replacement_cost),rating 
FROM film 
GROUP BY rating 

-- We can round off the repalcement_cost
SELECT ROUND(AVG(replacement_cost)),rating 
FROM film 
GROUP BY rating 

-- CHALLENGE 3

-- We are runninng a promotion to reward our top 5 customers with cupons 
-- what is the customer ids of the top 5 customers by total spend 
SELECT * FROM payment

SELECT customer_id,SUM(amount)
FROM payment 
GROUP BY customer_id
ORDER BY SUM(amount) DESC
limit 5


SELECT customer_id FROM payment
GROUP BY customer_id

-- total amount spend by each customer 
SELECT customer_id FROM payment
GROUP BY customer_id
ORDER BY SUM(amount)

SELECT customer_id,SUM(amount) 
FROM payment 
WHERE customer_id NOT IN (184,87,477)
GROUP BY customer_id

-- using "HAVING " clause
SELECT customer_id,SUM(amount)
FROM payment
GROUP BY customer_id
HAVING SUM(amount) > 100


--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
-- Challenge on HAVING 

/*  we are launching a platinum service for our most loyal customers. 
We will assign platinum status to cutomers that have had 40 or more transaction 
payments. 
What cutomer_id's are eligible for platinums status?
*/

SELECT customer_id, COUNT(*) 
FROM payment 
GROUP BY customer_id 
HAVING COUNT(*) >= 40


/*  
What are the customer ids of customers who have to spent more than $100 
in payment transactions with our staff_id memeber 2
*/
SELECT customer_id, SUM(amount)
FROM payment 
WHERE staff_id = 2 
GROUP BY customer_id 
HAVING SUM(amount) > 100



