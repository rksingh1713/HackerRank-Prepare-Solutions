SELECT
    CEILING( (
            SUM(Salary) - SUM(
                REPLACE
(Salary, '0', "")
            )
        ) / COUNT(*)
    )
FROM EMPLOYEES;