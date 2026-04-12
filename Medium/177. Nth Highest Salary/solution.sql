CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) RETURNS TABLE (Salary INT) AS $$
BEGIN
IF N < 1 THEN
    RETURN QUERY(SELECT NULL::INT AS salary);
ELSE
  RETURN QUERY (
    SELECT DISTINCT Employee.salary from Employee order by salary desc limit 1 offset N-1  
  );
  END IF;
END;
$$ LANGUAGE plpgsql;
