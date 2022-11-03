#创建Department表
create table Department184(
	id int(4) primary key,
	name VARCHAR(20)
);

show create table Department184;

insert into Department184 values
	(1,'IT'),
	(2,'Sales')
	;

select * from Department184;

#创建Employee表
create table Employee184(
	id int(4) primary key, 
	name varchar(20),
	salary int(10),
	departmentId int(4),
	constraint fk_emp_dept foreign key(departmentId) references Department184(id)
);

show create table Employee184;

insert into Employee184 values
	(1,'Joe',70000,1),
	(2,'Jim',90000,1),
	(3,'Henry',80000,2),
	(4,'Sam',60000,2),
	(5,'Max',90000,1)
	;
	
select * from Employee184;

# Write an SQL query to find employees who have the highest salary in each of the departments.
# solution1---inner join SQL92 & 子查询
select
	d.name as Department,
	e.name as Employee,
	e.salary as salary
from 
	Employee184 e, Department184 d 
where
	e.departmentId=d.id 
and 
	(e.departmentId,e.salary) in (select departmentId,max(salary) from Employee184 group by departmentId);

# solution2---inner join SQL99 & 子查询
select
	d.name as Department,
	e.name as Employee,
	e.salary as salary
from 
	Employee184 e join Department184 d 
on
	e.departmentId=d.id 
where 
	salary >= (select max(salary) from Employee184 where departmentId=d.id);
	
# solution3---窗口函数dense_rank() & left join
#此方法较灵活，可通过更改DenseRank的赋值来获得不同的排名工资
select
	s.Department,
	s.Employee,
	s.Salary
from (
	select
		d.name as Department,
		e.name as Employee,
		e.salary as salary,
		dense_rank() over(partition by e.departmentId order by e.salary desc) DenseRank 
	from 
		Employee184 e left join Department184 d
	on 
		e.departmentId=d.id) s
where 
	DenseRank=1;