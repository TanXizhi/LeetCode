create table Scores(
	id int(4) primary key,
	score decimal(3,2)
);

show create table Scores;

insert into Scores values
	(1,3.50),
	(2,3.65),
	(3,4.00),
	(4,3.85),
	(5,4.00),
	(6,3.65)
	;

select * from Scores;

# Return the result table ordered by score in descending order
# Solution 1: use dense_rank() function
# rank也是函数，如果要将rank作为命名，这里需要加引号否则会报错
select 
	score,dense_rank() over (order by score desc) 'rank' 
from 
	Scores;
	
	
# Solution 2 
select
	a.score,count(distinct b.score) 'rank'
from 
	Scores a, Scores b
where 
	a.score <= b.score
group by 
	a.id
order by 
	a.score desc;
	
# Solution 3 
select
	score,(select count(distinct score) from Scores where score >= s.score) 'rank'
from 
	Scores s
order by 
	score desc;
	
	
# SQL中的排序函数：DENSE_RANK()、RANK()和row_number()

#语法
#row_number() over(order by 列名) ---> row_number():不考虑数据的重复性 按照顺序一次打上标号,如:1，2，3，4
#rank() over(order by 列名) ---> RANK()是跳跃排序,如：1 2 2 4,会跳过3
#dense_rank() over( order by 列名) ---> DENSE_RANK()是连续排序,如: 1 2 2 3 序号连续
    











