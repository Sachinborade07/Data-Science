-- select people either unde 30 over over 50 with an income above 50000 that are
-- either Japan or Australia 

select * from customers

select firstname, income, age from customers 
where income > 50000 AND (age <= 30  OR age >= 50 )
AND (country = 'Japan' OR country = 'Australia')

-- what was our total sales in June of 2004 for orders over 100 dollars?

select SUM(totalamount) from orders
where (orderdate >= '2004-06-01' AND orderdate <= '2004-06-30')
AND totalamount > 100 






