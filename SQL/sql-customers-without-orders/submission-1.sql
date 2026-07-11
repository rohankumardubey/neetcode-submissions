-- Write your query below

select name 
from customers 
group by 1 

EXCEPT

select 
customer.name
from customers as customer
inner join orders as orders
on orders.customer_id = customer.id
group by 1