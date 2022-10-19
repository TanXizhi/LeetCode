create table Person(
	id int(4),
	email varchar(30)
);

show create table Person;

insert into Person values
	(1, 'john@example.com'),
	(2, 'bob@example.com'),
	(3, 'john@example.com');

select * from Person;


---自连接
delete 
	p1 
from 
	Person p1, Person p2 
where 
	p1.email=p2.email and p1.id > p2.id;
	

---子查询
delete 
from 
	Person 
where 
	id not in (
	select 
		id 
	from 
		(select min(id) id from Person group by email)tt);
