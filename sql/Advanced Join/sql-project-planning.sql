SELECT
    A.START_DATE,
    MIN(B.END_DATE)
FROM (
        SELECT A.END_DATE
        FROM PROJECTS AS A
        WHERE
            DATE_ADD(A.END_DATE, INTERVAL 1 DAY) NOT IN (
                SELECT
                    DISTINCT A2.END_DATE
                FROM
                    PROJECTS AS A2
            )
    ) AS B, (
        SELECT A.START_DATE
        FROM PROJECTS AS A
        WHERE
            DATE_SUB(A.START_DATE, INTERVAL 1 DAY) NOT IN (
                SELECT
                    DISTINCT A1.START_DATE
                FROM
                    PROJECTS AS A1
            )
    ) AS A
WHERE A.START_DATE < B.END_DATE
GROUP BY A.START_DATE
ORDER BY
    DATEDIFF(MIN(B.END_DATE), A.START_DATE),
    A.START_DATE