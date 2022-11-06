#创建Customers表
create table Customers(
	id int(4) primary key,
	name VARCHAR(10)
);

show create table Customers;

insert into Customers values
	(1,'Joe'),
	(2,'Henry'),
	(3,'Sam'),
	(4,'Max')
	;

select * from Customers;

#创建Orders表
create table Orders(
	id int(4) primary key, 
	customerId int(4),
	constraint fk_cus_ord foreign key(customerId) references Customers(id)
);

show create table Orders;

insert into Orders values
	(1,3),
	(2,1)
	;
	
select * from Orders;

#Write an SQL query to report all customers who never order anything.
#Solution1 
select 
	c.name as Customers
from 
	Customers c
where 
	c.id not in (select customerId from Orders;


#Solution2 left join + is null
select 
	c.name as Customers
from 
	Customers c left join Orders o
on 
	c.id=o.customerId
where 
	o.customerId is null;