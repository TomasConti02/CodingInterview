#SQL — join employee and department

SELECT *
FROM employee e 
join department d on e.department_id==d.id
#LEFT JOIN
#If you want employees even when they don't have a department:
select *
from employee e
left join department d on e.department_id==d.id