create table Employee(
	id int(4) primary key,
	salary int(10)
);

show create table Employee;

insert into Employee values
	(1,400),
	(2,200),
	(3,200),
	(4,300),
	(5,100)
	;

select * from Employee;

---Report the second highest salary from the Employee table. If there is no second highest salary, the query should report null.
---Solution1
select 
	(select distinct
		salary
	from 
		Employee 
	order by 
		salary desc 
	limit 1 offset 1) as SecondHighestSalary;
	
---Solution2 (Best)
select ifnull(
	(select distinct
		salary
	from 
		Employee 
	order by 
		salary desc 
	limit 1 offset 1),null) as SecondHighestSalary;

---Solution3
select 
	max(salary) as SecondHighestSalary
from 
		Employee 
where
	salary < (select max(salary) from Employee);