create table Courses(
	student varchar(20),
	class varchar(20),
	primary key(student,class)
);

show create table Courses;

insert into Courses values
	('A','Math'),
	('B','English'),
	('C','Math'),
	('D','Biology'),
	('E','Math'),
	('F','Computer'),
	('G','Math'),
	('H','Math'),
	('I','Math')
	;

select * from Courses;

select 
	class 
from 
	Courses 
group by 
	class 
having 
	count(distinct student) >= 5;