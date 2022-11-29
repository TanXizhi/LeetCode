create table Seat(
	id int(4) primary key auto_increment,
	student varchar(20)
);

show create table Seat;

insert into Seat values
	(1,'Abbot'),
	(2,'Doris'),
	(3,'Emerson'),
	(4,'Green'),
	(5,'Jeames')
	;

select * from Seat;


#Write an SQL query to swap the seat id of every two consecutive students. 
#If the number of students is odd, the id of the last student is not swapped.
#Solution1 
select (case 
					when mod(id,2)=1 and id=(select count(*) from seat) then id
					when mod(id,2)=1 then id+1
					else id-1
				end) as id, student 
from 
	Seat 
order by 
	id;
	
#Solution2
#利用异或只把偶数减2,奇数不变,从而调位.（单数-1后，最后一位是0，异或把最后一位变回1，等于不变；偶数-1后，最后一位是1，异或把最后一位变成0，等于再减去1）
select
	rank() over(order by (id-1)^1) as id, student 
from 
	Seat;