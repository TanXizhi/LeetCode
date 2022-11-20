create table Orders586(
	order_number int(4) primary key,
	customer_number int(4)
);

show create table Orders586;

insert into Orders586 values
	(1,1),
	(2,2),
	(3,3),
	(4,3)
	;

select * from Orders586;




#Write an SQL query to find the customer_number for the customer who has placed the largest number of orders.
#solution1
select 
	customer_number 
from 
	Orders586 
group by 
	customer_number 
order by 
	count(customer_number) desc 
limit 0,1



#solution2
select 
	customer_number
from 
	Orders586 
group by 
	customer_number
having count(customer_number) = (
    select max(sum) 
    from (
        select count(customer_number) as sum
        from Orders586
        group by customer_number
    )tmp
);