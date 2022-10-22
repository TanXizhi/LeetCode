create table Person1(
	PersonId int(4) primary key,
	FirstName varchar(30),
	LastName varchar(30)
);

show create table Person1;


create table Address(
	AddressId int(4) primary key,
	PersonId int(4),
	City varchar(30),
	State varchar(30)
);

show create table Address;


insert into Person1 values
	(1, 'Allen', 'Wang'),
	(2, 'Bob', 'Alice');

select * from Person1;


insert into Address values
	(1, 2, 'New York City', 'New York'),
	(2, 3, 'Los Angeles', 'California');

select * from Address;


---外连接
select 
	p.FirstName,p.LastName,a.City,a.State 
from 
	Person1 p left join Address a 
on 
	p.PersonId=a.PersonId;