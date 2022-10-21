create table Weather(
	id int primary key,
	recordDate date,
	temperature int
);

show create table Weather;

insert into Weather values
	(1, '2015-01-01', 10),
	(2, '2015-01-02', 25),
	(3, '2015-01-03', 20),
	(4, '2015-01-04', 30);

select * from Weather;

---自连接（SQL92）
select 
	b.id as id 
from 
	Weather a, Weather b
where 
	datediff(b.recordDate,a.recordDate)=1 and b.temperature > a.temperature;
	
---自连接（SQL99）
select 
	b.id as id 
from 
	Weather a join Weather b
on
	datediff(b.recordDate,a.recordDate)=1 
where
	b.temperature > a.temperature;
	
	
	
	
---subquery子函数,用lag()开窗函数配合datediff()函数
select 
	id 
from 
	(select 
		id,
		temperature,
		recordDate,
    lag(recordDate,1) over(order by recordDate) as last_date,
		lag(temperature,1) over(order by recordDate) as last_temperature
	from Weather)tt
where 
	datediff(recordDate,last_date)=1 and temperature > last_temperature;
		
