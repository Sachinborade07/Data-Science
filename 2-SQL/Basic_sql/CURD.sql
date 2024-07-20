-- PERFORMING THE CURD OPERATION USING SQL 

CREATE TABLE account(
	user_id SERIAL PRIMARY KEY,
	user_name VARCHAR(50) UNIQUE NOT NULL,
	password VARCHAR(50) NOT NULL,
	email VARCHAR(50) UNIQUE NOT NULL,
	created_on TIMESTAMP NOT NULL,
	last_login TIMESTAMP
);

SELECT * FROM account

-----------------------------------------------------------------------------

-- creating another table 
CREATE TABLE job(
	job_id SERIAL PRIMARY KEY,
	job_name VARCHAR(100) UNIQUE NOT NULL
);

SELECT * FROM job

-----------------------------------------------------------------------------

-- creating table account job 
CREATE TABLE account_job(
	user_id INTEGER REFERENCES account(user_id),
	job_id INTEGER REFERENCES job(job_id),
	hire_date TIMESTAMP
)

SELECT * FROM account_job

-----------------------------------------------------------------------------
-----------------------------------------------------------------------------
 
-- INSERTING INTO TABLE 

----
SELECT * FROM account -- it is empty 

INSERT INTO account(user_name, password,email,created_on)
VALUES 
('Jose','password','jose@gmail.com',CURRENT_TIMESTAMP)

SELECT * FROM account -- not it has some values 
----

INSERT INTO job(job_name) 
VALUES
('Astronaut')

SELECT * FROM job

INSERT INTO job(job_name) 
VALUES
('President')

SELECT * FROM job

INSERT INTO account_job(user_id,job_id,hire_date)
VALUES 
(1,1,CURRENT_TIMESTAMP);

SELECT * FROM account_job

INSERT INTO account_job(user_id,job_id,hire_date)
VALUES 
(10,10,CURRENT_TIMESTAMP); -- here we are getting error because violates foreign key constraint 

SELECT * FROM account_job

INSERT INTO account(user_name, password,email,created_on)
VALUES 
('Sachin','root','sachinborade195@gmail.com',CURRENT_TIMESTAMP)

-- checking the account table 
SELECT * FROM account 

-- inserting more values 
INSERT INTO job(job_name)
VALUES ('DATA SCIENTIST')

SELECT * FROM job

---

-----------------------------------------------------------------------------
-----------------------------------------------------------------------------

-- UPDATING INTO TABLE 

----

UPDATE account
SET last_login = CURRENT_TIMESTAMP

SELECT * FROM account
--------

UPDATE account 
SET last_login = created_on

SELECT * FROM account
--------

SELECT * FROM account_job

UPDATE account_job
SET hire_date = account.created_on 
FROM account
WHERE account_job.user_id = account.user_id

SELECT * FROM account_job
--------

-----------------------------------------------------------------------------
-----------------------------------------------------------------------------

-- DELETE INTO TABLE 

-- 10/7/24

SELECT * FROM job

-- INSERTING 
INSERT INTO job(job_name) VALUES ('Cowboy')
SELECT * FROM job

-- DELETING 
DELETE FROM job 
WHERE job_name = 'Cowboy'
RETURNING job_id, job_name

SELECT * FROM job

-----------------------------------------------------------------------------
-----------------------------------------------------------------------------

CREATE TABLE information (
info_id SERIAL PRIMARY KEY,
title VARCHAR(500) NOT NULL,
person VARCHAR(500) NOT NULL UNIQUE
)

SELECT * FROM information 

------------------------------

-- ALTER INTO TABLE 

ALTER TABLE information 
RENAME TO new_info

SELECT * FROM information  --- error because the table named changed.
SELECT * FROM new_info		

------------------------------

ALTER TABLE new_info
RENAME COLUMN person TO people

------------------------------
INSERT INTO new_info(title)
VALUES 
('some new title') 
--- here we are getting the error beacuse "people"
-- column can't have neagtive values

ALTER TABLE new_info
ALTER COLUMN people DROP NOT NULL 

SELECT * FROM new_info

INSERT INTO new_info(title)
VALUES 
('some new title') -- now you will not get the error
------------------------------

SELECT * FROM new_info

ALTER TABLE new_info
DROP COLUMN people
-- here we can see the "people" table is not dropped
SELECT * FROM new_info

ALTER TABLE new_info
DROP COLUMN people 
-- ERROR:  column "people" of relation "new_info" does not exist 

ALTER TABLE new_info
DROP COLUMN IF EXISTS people 
-- NOTICE:  column "people" of relation "new_info" does not exist, skipping ALTER TABLE


-----------------------------------------------------------------------------
-----------------------------------------------------------------------------

CREATE TABLE employees(
	emp_id SERIAL PRIMARY KEY,
	first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50) NOT NULL,
	birthdate DATE CHECK (birthdate > '1900-01-01'),
	hire_date DATE CHECK (hire_date > birthdate),
	salary INTEGER CHECK (salary > 0)
);
SELECT * FROM employees

INSERT INTO employees( first_name,last_name,birthdate,hire_date,salary )
VALUES ('Sachin','Borade','2004-02-01','2021-01-01',100000)  -- INSERTED SUCCESSFULLY

INSERT INTO employees( first_name,last_name,birthdate,hire_date,salary )
VALUES ('Jose','Pablo','1890-02-01','2010-01-01',100) 
-- violates check constraint "employees_birthdate_check"

INSERT INTO employees( first_name,last_name,birthdate,hire_date,salary )
VALUES ('Jose','Pablo','1990-02-01','2010-01-01',100) -- INSERTED SUCCESSFULLY

INSERT INTO employees( first_name,last_name,birthdate,hire_date,salary )
VALUES ('Sachin','Borade','2004-02-01','2021-01-01',-100)  
-- violates check constraint "employees_salary_check"

SELECT * FROM employees
