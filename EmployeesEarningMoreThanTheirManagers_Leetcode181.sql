create table Employee(
	id int(4) primary key,
	name VARCHAR(20),
	salary int(10),
	managerId int(5)
);

show create table Employee;

insert into Employee values
	(1,'Joe',70000,3),
	(2,'Henry',80000,4),
	(3,'Sam',60000,NULL),
	(4,'Max',90000,Null)
	;

select * from Employee;

# Write an SQL query to find the employees who earn more than their managers
# 自连接---SQL92
select
	e.name as Employee
from 
	Employee e,Employee m 
where 
	e.managerId=m.id and e.salary > m.salary;

# 自连接---SQL99
select
	e.name as Employee
from 
	Employee e join Employee m 
on 
	e.managerId=m.id and e.salary > m.salary;
	
# 子连接
select
	name as Employee
from 
	Employee e
where 
	salary > (select salary from Employee where id = e.managerId);