#创建Department表
create table Department185(
	id int(4) primary key,
	name VARCHAR(20)
);

show create table Department185;

insert into Department185 values
	(1,'IT'),
	(2,'Sales')
	;

select * from Department185;

#创建Employee表
create table Employee185(
	id int(4) primary key, 
	name varchar(20),
	salary int(10),
	departmentId int(4),
	constraint fk_emp185_dept185 foreign key(departmentId) references Department185(id)
);

show create table Employee185;

insert into Employee185 values
	(1,'Joe',85000,1),
	(2,'Henry',80000,2),
	(3,'Sam',60000,2),
	(4,'Max',90000,1),
	(5,'Janet',69000,1),
	(6,'Randy',85000,1),
	(7,'Will',70000,1)
	;
	
select * from Employee185;

#A company's executives are interested in seeing who earns the most money in each of the company's departments.
#A high earner in a department is an employee who has a salary in the top three unique salaries for that department.
#Write an SQL query to find the employees who are high earners in each of the departments.
#Solution1
select 
	d.name as Department, e.name as Employee, e.salary as Salary
from 
	Department185 as d 
	join
	(select 
		name, salary, departmentId, dense_rank() over(partition by departmentId order by salary desc) as DenseRank 
	from 
		Employee185) as e
on 
	e.departmentid=d.id 
where 
	e.DenseRank <=3;
	
	
#Solution2
select
	d.name as Department, e1.name as Employee, e1.salary as Salary
from
	Employee185 e1
	join
	Department185 as d 
on 
	e1.departmentid=d.id 
where 3 >
	(select count(distinct e2.salary)
	from Employee185 e2
	where e2.salary > e1.salary and e1.departmentId=e2.departmentId)
;
