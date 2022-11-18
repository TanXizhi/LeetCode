create table Activity(
	player_id int(4),
	device_id int(4),
	event_date date,
	games_played int(4),
	primary key(player_id, event_date)
);

show create table Activity;

insert into Activity values
	(1,2,'2016-03-01',5),
	(1,2,'2016-05-02',6),
	(2,3,'2017-06-25',1),
	(3,1,'2016-03-02',0),
	(3,4,'2018-07-03',5)
	;

select * from Activity;

# Write an SQL query to report the first login date for each player.
# Solution 1
select 
	t.player_id, t.event_date 'first_login'
from 
	(select player_id, dense_rank() over (partition by player_id order by event_date)'dense_rank',event_date from Activity) t
where
	t.dense_rank = 1
	
# Solution 2
select 
	player_id, min(event_date) 'first_login'
from 
	Activity
group by 
	player_id;
	
# Solution 3	
select 
	distinct player_id, min(event_date) over (partition by player_id) 'first_login'
from 
	Activity;
	