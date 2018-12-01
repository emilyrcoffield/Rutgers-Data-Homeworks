-- USE SAKILA Database
USE SAKILA;
SHOW TABLES;
-- Question 1a:
-- SELECT first_name,last_name
-- FROM actor;

-- Question 1b:
-- SELECT UPPER(CONCAT(first_name,' ',last_name)) as ACTOR_NAME 
-- FROM Actor

-- Question 2a:
-- SELECT * FROM actor;
-- SELECT first_name, last_name, actor_id 
-- FROM actor
-- WHERE first_name = "Joe";

-- Question 2b:
-- SELECT first_name, last_name, actor_id
-- FROM actor
-- WHERE last_name like "%GEN%";

-- Question 2c:
-- SELECT first_name, last_name, actor_id
-- FROM actor
-- WHERE last_name like "%LI%"
-- ORDER BY last_name, first_name;

-- Question 2d:
-- SELECT country_id, country
-- FROM country
-- WHERE country in ('Afghanistan','Bangladesh','China')

-- Question 3a:
-- ALTER TABLE actor
-- Add column description BLOB

-- Question 3b:
-- ALTER TABLE actor
-- DROP COLUMN description;

-- Question 4a:
-- SELECT last_name, COUNT(*) AS 'Number of Actors' 
-- FROM actor GROUP BY last_name;

-- Question 4b:
-- SELECT last_name, COUNT(*) AS 'Number of Actors' 
-- FROM actor GROUP BY last_name HAVING count(*) >=2;

-- Question 4c:
-- UPDATE actor
-- SET first_name = 'HARPO'
-- WHERE first_name = 'GROUCHO'
-- and last_name = 'WILLIAMS';

-- Question 4d:
-- UPDATE Actor 
-- Set first_name = 
-- CASE
-- WHEN first_name = 'HARPO' THEN 'GROUCHO'
-- ELSE 'MUCHO GROUCHO'
-- END
-- WHERE actor_id = 172;

-- Question 5a:
-- SHOW CREATE TABLE address;

-- Question 6a:
-- SELECT s.first_name, s.last_name, a.address
-- FROM staff s
-- INNER JOIN address a
-- ON (s.address_id = a.address_id);

-- Question 6b:
-- SELECT payment.staff_id, staff.first_name, staff.last_name, payment.amount, payment.payment_date
-- FROM staff INNER JOIN payment ON
-- staff.staff_id = payment.staff_id AND payment_date LIKE '2005-08%'; 

-- Question 6c:
-- SELECT f.title, COUNT(fa.actor_id) AS 'Actors'
-- FROM film_actor AS fa
-- INNER JOIN film as f
-- on f.film_id = fa.film_id
-- GROUP BY f.title
-- ORDER BY Actors desc;

-- Question 6d:
-- SELECT title, COUNT(inventory_id) AS '# of copies'
-- from film
-- INNER JOIN inventory
-- USING ( film_id)
-- WHERE title = 'Hunchback Impossible'
-- GROUP BY title;

-- Question 6e:
-- SELECT c.first_name, c.last_name, SUM(p.amount) AS 'Total Amount Paid'
-- FROM payment As p
-- JOIN customer As c
-- on p.customer_id = c.customer_id
-- GROUP BY c.customer_id
-- ORDER BY c.last_name;

-- Question 7a:
-- SELECT TITLE
-- FROM film
-- WHERE title LIKE 'K%'
-- OR title LIKE 'Q%'
-- AND language_id IN
-- (
--  SELECT language_id
--  FROM language
--  WHERE name = 'English'
-- );

-- Question 7b:
-- SELECT first_name, last_name
-- FROM actor
-- WHERE actor_id IN
-- (
-- SELECT actor_id
-- FROM film_actor
-- WHERE film_id =
--  (
--    SELECT film_id
--    FROM film
--    WHERE title = "Alone Trip"
--  )
--  );
 

-- Question 7c:
-- SELECT first_name, last_name,email, country,
-- FROM customer cus,
-- JOIN address a
-- ON (cus.address_id = a.address_id)
-- JOIN city cit
-- ON (a.city_id = cit.city_id)
-- JOIN country ctr
-- ON (cit.country_id = ctr.country_id)
-- WHERE ctr.country = 'canada';

-- Question 7d:
-- SELECT title, c.name
-- FROM film f
-- JOIN film,category fc
-- ON (f.film_id = fc.film_id)
-- JOIN category c
-- ON (c.category_id = fc.category_id_
-- WHERE name = 'family';

-- Question 7e:
-- SELECT title, COUNT(title) as 'Rentals'
-- FROM film
-- JOIN inventory
-- on(film.film_id = inventory.film_id)
-- JOIN rental
-- ON (inventory.inventory_id = rental.inventory_id)
-- GROUP by title
-- ORDER BY rentals desc;

-- Question 7f:
-- SELECT s.store_id, SUM(amount) AS Gross
-- FROM payment p
-- JOIN rental r
-- ON (p.rental_id = r.rental_id)
-- JOIN inventory i
-- ON ( i.inventory_id = r.inventory_id)
-- JOIN store s
-- ON (s.store_id = i.store_id)
-- GROUP BY s.store_id;

-- Question 7g:
-- SELECT store_id, city, country
-- FROM store s,
-- JOIN address a
-- ON (s.address_id = a.address_id); 

-- Question 7h:
--  SELECT name AS Genre, concat('$',format(SUM(amount),2)) AS Gross_Revenue FROM category
--  JOIN film_category ON category.category_id=film_category.category_id
--  JOIN inventory ON film_category.film_id=inventory.film_id
--  JOIN rental ON inventory.inventory_id=rental.inventory_id
--  JOIN payment ON rental.rental_id=payment.rental_id
--  GROUP BY Genre
--  ORDER BY SUM(amount) DESC
--  LIMIT 5

-- Question 8a:
--  CREATE VIEW AS top_five_genres AS
--  SELECT SUM(amount) AS 'TOTAL Sales', c.name AS 'GENRE'
--  FROM payment p
--  JOIN rental r
--  on (p.rental_id = r.rental_id)
--  JOIN inventory i
--  on (r.inventory_id = i.inventory_id)
--  JOIN film_category fc  
--  on(i.film_id = fc.film_id)
--  JOIN category c
--  ON (fc.category_id = c.category_id)
--  GROUP BY c.name
--  ORDER BY SUM(amount) DESC
--  LIMIT 5

-- Question 8b:
--  SELECT * FROM top_five_genres

-- Question 8c:
--  DROP VIEW top_five_genres