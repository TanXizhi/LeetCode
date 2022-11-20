create table Customer584(
	id int(4) primary key,
	name varchar(20),
	referee_id int(4)
);

show create table Customer584;

insert into Customer584 values
	(1,'Will',null),
	(2,'Jane',null),
	(3,'Alex',2),
	(4,'Bill',null),
	(5,'Zack',1),
	(6,'Mark',2)
	;

select * from Customer584;


#Write an SQL query to report the names of the customer that are not referred by the customer with id = 2.
#solution1 
select 
	name 
from 
	Customer584 
where 
	ifnull(referee_id,0) != 2;
	
#solution2
select 
	name 
from 
	Customer584 
where 
	id not in (select id from Customer584 where referee_id = 2);