create table Tree(
	id int(4) primary key,
	p_id int(4)
);

show create table Tree;

insert into Tree values
	(1,null),
	(2,1),
	(3,1),
	(4,2),
	(5,2)
	;

select * from Tree;


# Write an SQL query to report the type of each node in the tree.
#Return the result table ordered by id in ascending order.
"""
Each node in the tree can be one of three types:
			"Leaf": if the node is a leaf node.	
			"Root": if the node is the root of the tree.
			"Inner": If the node is neither a leaf node nor a root node.
"""

#solution1---case when 条件
"""
需要将p_id为null的情况筛除，原因是当询问id not in (select p_id from tree)时, 
因为p_id有null值, 返回结果全为false, 于是跳到else的结果, 返回值为inner. 
所以在答案中,leaf结果从未彰显,全被inner取代.
"""
select 
	id, 
	case when p_id is null then 'Root'
			 when id not in (select p_id from Tree where p_id is not null) then 'Leaf'
			 else 'Inner'
	 end as type 
from 
	Tree;
	
#solution2---case when 条件
select 
	id, 
	case when p_id is null then 'Root'
			 when id in (select p_id from Tree) and p_id is not null then 'Inner'
			 else 'Leaf'
	 end as type 
from 
	Tree;
	
#solution3---if
select 
	id, 
	if(isnull(p_id), 'Root', if(id in (select p_id from Tree), 'Inner', 'Leaf')) as type
from 
	Tree
order by 
	id;
 
#solution4---union
select 
	id, 'Root' as type
from 
	Tree
where
	p_id is null 
union 
select 
	id, 'Leaf' as type
from 
	Tree
where
	id not in (select p_id from Tree where p_id is not null)
union 
select 
	id, 'Inner' as type
from 
	Tree
where
	id in (select p_id from Tree)
	and 
	p_id is not null
order by 
	id;
 
		 
