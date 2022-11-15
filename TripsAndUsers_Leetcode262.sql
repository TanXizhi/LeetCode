#创建Orders表
create table Users(
	users_id int(4) primary key, 
	banned enum('Yes','No'),
	role enum('client','driver','partner')
);

show create table Users;

insert into Users values
	(1,'No','client'),
	(2,'Yes','client'),
	(3,'No','client'),
	(4,'No','client'),
	(10,'No','driver'),
	(11,'No','driver'),
	(12,'No','driver'),
	(13,'No','driver')
	;
	
select * from Users;

#创建Trips表
create table Trips(
	id int(4) primary key,
	client_id int(4),
	driver_id int(4),
	city_id int(4),
	status enum('completed','cancelled_by_driver','cancelled_by_client'),
	request_at date,	
	constraint fk_tr_ur1 foreign key(client_id) references Users(users_id),
	constraint fk_tr_ur2 foreign key(driver_id) references Users(users_id)
);


show create table Trips;

insert into Trips values
	(1,1,10,1,'completed','2013-10-01'),
	(2,2,11,1,'cancelled_by_driver','2013-10-01'),
	(3,3,12,6,'completed','2013-10-01'),
	(4,4,13,6,'cancelled_by_client','2013-10-01'),
	(5,1,10,1,'completed','2013-10-02'),
	(6,2,11,6,'completed','2013-10-02'),
	(7,3,12,6,'completed','2013-10-02'),
	(8,2,12,12,'completed','2013-10-03'),
	(9,3,10,12,'completed','2013-10-03'),
	(10,4,13,12,'cancelled_by_driver','2013-10-03')
	;

select * from Trips;





#Write a SQL query to find the cancellation rate of requests with unbanned users (both client and driver must not be banned) 
#each day between "2013-10-01" and "2013-10-03". Round Cancellation Rate to two decimal points.

#Solution1
SELECT
		request_at 'Day', round(avg(status!='completed'), 2) 'Cancellation Rate'
FROM Trips t 
    JOIN Users u1 ON (t.client_id = u1.users_id AND u1.banned = 'No')
    JOIN Users u2 ON (t.driver_id = u2.users_id AND u2.banned = 'No')
WHERE	
    request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY 
    request_at;
		

#Solution2
SELECT
		request_at 'Day', round(sum(if(t.status='completed',0,1))/count(t.status),2) 'Cancellation Rate'
FROM Trips t 
    JOIN Users u1 ON (t.client_id = u1.users_id AND u1.banned = 'No')
    JOIN Users u2 ON (t.driver_id = u2.users_id AND u2.banned = 'No')
WHERE	
    request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY 
    request_at;
		

#Solution3
SELECT
		T.request_at 'Day', round(sum(if(T.status='completed',0,1))/count(T.status),2) 'Cancellation Rate'
FROM Trips AS T
WHERE 
	T.client_Id not IN (
		SELECT users_id
		FROM users
		WHERE banned = 'Yes'
)
AND
	T.driver_Id not IN (
		SELECT users_id
		FROM users
		WHERE banned = 'Yes'
)
AND T.request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY 
	T.request_at;

