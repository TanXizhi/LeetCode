create table Person(
	id int(4) primary key,
	email VARCHAR(30)
);

show create table Person;

insert into Person values
	(1,'a@b.com'),
	(2,'c@d.com'),
	(3,'a@b.com')
	;

select * from Person;

#Write an SQL query to report all the duplicate emails
#solution1 group by + having
select 
	email as Email 
from 
	Person 
group by 
	email 
having 
	count(email)>1;

#solution2 rank()
select 
	distinct(d.email) as Email 
from 
	(select email, rank() over(partition by email order by id) r from Person) d 
where 
	d.r>1;

#solution3 子表查询+count()
select 
	d.email as Email 
from 
	(select count(email) as num,email from person group by email) d 
where 
	d.num>1;
	
#solution4 自连接
select 
	distinct(a.email) as Email 
from 
	Person a, Person b
where 
	a.email=b.email and a.id != b.id;

