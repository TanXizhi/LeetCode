create table Logs(
	id int(4) primary key auto_increment,
	num VARCHAR(20)
);

show create table Logs;

insert into Logs values
	(1,1),
	(2,1),
	(3,1),
	(4,2),
	(5,1),
	(6,2),
	(7,2)
	;

select * from Logs;

# Write an SQL query to find all numbers that appear at least three times consecutively.
# Solution1 
select distinct l1.num as ConsecutiveNums 
from 
	Logs l1,
	Logs l2,
	Logs l3
where 
	l1.id+1=l2.id 
	and l2.id+1=l3.id 
	and l1.num=l2.num
	and l2.num=l3.num
;

# Solution2 (利用窗口函数lag()和lead())
select distinct num as ConsecutiveNums 
from 
	(select num, 
					lag(num,1,null) over(order by id) lag_num, 
					lead(num,1,null) over(order by id) lead_num
	from
		Logs) l		
where 
	l.num=l.lag_num and l.num=l.lead_num
;

# Solution3 (此方法适用于id不连续的情况，解决方式是通过重新生成连续id2来实现)
select distinct num as ConsecutiveNums 
from 
	(select *, 
					row_number() over(partition by num order by id) rownum, 
					row_number() over(order by id) id2
	from
		Logs) l		
group by 
	num,id2-rownum 
having 
	count(*)>=3
;
	