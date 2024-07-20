SHOW TIMEZONE


CREATE TABLE timezones(
	ts TIMESTAMP WITHOUT TIME ZONE,
	tz TIMESTAMP WITH TIME ZONE
)
SELECT * FROM timezones


INSERT INTO timezones VALUES(
	TIMESTAMP WITHOUT TIME ZONE '2023-03-07 10:50',
	TIMESTAMP WITH TIME ZONE '2023-03-07 10:50'
) 
SELECT * FROM timezones


--getting the todays date 
SELECT now()::date;
SELECT CURRENT_DATE

-- getting the todays date in date/month/year format
SELECT TO_CHAR(CURRENT_DATE,'dd/mm/yy')

-- to get the value of days 
SELECT TO_CHAR(CURRENT_DATE,'ddd')

SELECT TO_CHAR(CURRENT_DATE,'ww')

-- finding the date of birth
SELECT AGE(date'1800-01-01')
SELECT AGE(date'2004-02-01')

-- finding the interval between the birth dates
SELECT AGE(date '1992/11/13',date'1800/01/01')

SELECT EXTRACT(DAY FROM date'1992/11/13') AS DAY 

SELECT EXTRACT(MONTH FROM date'1992/11/13') AS MONTH

SELECT EXTRACT(YEAR FROM date'1992/11/13') AS YEAR

SELECT DATE_TRUNC('year',date'1992/11/13')


--Q) Get me all the employees above 60, use appropriate date function 
SELECT AGE(birth_date), * FROM employees
WHERE(
	EXTRACT (YEAR FROM AGE(birth_date))
)>60;


SELECT COUNT(birth_date) FROM employees
WHERE birth_date<now()-INTERVAL'61 years'

-- Q) How many employees were hired in february 
SELECT COUNT(emp_no) FROM employees
WHERE EXTRACT (MONTH FROM hire_date) = 2

-- Q3) How many employees were born in November
SELECT COUNT(emp_no) FROM employees
WHERE EXTRACT (MONTH FROM birth_date) =11

--Q4)  WHO IS OLDEST EMPLOYEE
SELECT MAX(AGE(birth_date)) FROM employees

SELECT MAX(salary) FROM salaries

-- I want to insert on column, which will having highest salary compared to other

SELECT *,
	MAX(salary) OVER()
	FROM salaries

-- APPLYING THE WINDOW SIZE OF 100
SELECT *,
	MAX(salary) OVER()
	FROM salaries
LIMIT 100

-- fetch the salary of the employees less than 70000 
SELECT *,
	MAX(salary) OVER()
	FROM salaries
WHERE salary<70000


SELECT *,
	AVG(salary) OVER()
FROM salaries


-- The average global salary across all the departments
SELECT *,
	d.dept_name,
	AVG(salary) OVER()
FROM salaries
JOIN dept_emp AS de USING (emp_no)
JOIN departments AS d USING (dept_no)

-- AVERAGE SALARY DEPT wise
SELECT *,
	d.dept_name,
	AVG(salary) OVER(
	PARTITION BY d.dept_name
	)
FROM salaries
JOIN dept_emp AS de USING (emp_no)
JOIN departments AS d USING (dept_no)

-- remove d.dept_name
SELECT *,
	AVG(salary) OVER(
	PARTITION BY d.dept_name
	)
FROM salaries
JOIN dept_emp AS de USING (emp_no)
JOIN departments AS d USING (dept_no)


/* what now? 
window functions create a new column
based on functions performed on a subset 
or "window" of the data -- quick reference 
*/

