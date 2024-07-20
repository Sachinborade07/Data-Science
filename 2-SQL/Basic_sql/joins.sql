-- Performing the INNER JOIN    8/7/24
SELECT * FROM payment -- TABLE 1 

SELECT * FROM customer -- TABLE 2 

SELECT payment_id, payment.customer_id,first_name 
FROM payment 
INNER JOIN customer 
ON payment.customer_id = customer.customer_id 

-- If we change the order of the table the result wont change 


SELECT payment_id, payment.customer_id,first_name 
FROM customer 
INNER JOIN payment
ON payment.customer_id = customer.customer_id 

---------------------------------------------------------------------------------

-- here we are performing FULL OUTER JOIN 
SELECT * FROM customer
FULL OUTER JOIN payment 
ON customer.customer_id = payment.customer_id 


---------------------------------------------------------------------------------

-- here we are performing LEFT OUTER JOIN 
SELECT film.film_id,title,inventory_id,store_id
FROM film 
LEFT JOIN inventory ON 
inventory.film_id = film.film_id 

-- now applying the where clause for LEFT OUTER JOIN 
SELECT film.film_id,title,inventory_id,store_id
FROM film 
LEFT JOIN inventory ON 
inventory.film_id = film.film_id 
WHERE inventory.film_id IS null
---------------------------------------------------------------------------------

-- here we are performing RIGHT JOIN 
-- same as LEFT OUTER JOIN so write RIGHT JOIN instead of LEFT JOIN
SELECT film.film_id,title,inventory_id,store_id
FROM film 
RIGHT JOIN inventory ON 
inventory.film_id = film.film_id 

-- applying the WHERE clause to RIGHT JOIN 
SELECT film.film_id,title,inventory_id,store_id
FROM film 
RIGHT JOIN inventory ON 
inventory.film_id = film.film_id 
WHERE inventory.film_id IS null


----------------------------------------------------------------------------------

-- Here we are performing the join operation 9/7/24

SELECT * FROM address 
INNER JOIN customer 
ON address.address_id = customer.customer_id
WHERE district = 'California'



-- CHALLENGE 1)
-- A customer walks in and is a huge of the actor 'Nick Wahlberg' and wants to know which movies he is in.
-- Get the list of all movies 

-- approach 
-- 1. 
select * from film 
-- 2. 
select * from actor 
-- 3. 
select * from film_actor 
--4. first inner join 
select * from actor 
inner join film_actor 
on actor.actor_id = film_actor.actor_id 
--5. our answer 
SELECT * FROM actor
INNER JOIN film_actor 
ON  actor.actor_id = film_actor.actor_id
INNER JOIN film 
ON film_actor.film_id = film.film_id 
--6. now apply the filter 
SELECT title,first_name,last_name FROM actor
INNER JOIN film_actor 
ON  actor.actor_id = film_actor.actor_id
INNER JOIN film 
ON film_actor.film_id = film.film_id 
WHERE first_name = 'Nick' AND last_name='Wahlberg'






