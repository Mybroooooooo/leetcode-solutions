select e.name from Employee e
where (select count(*) from Employee where managerId = e.id) >= 5
