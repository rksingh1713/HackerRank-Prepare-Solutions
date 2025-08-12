WITH PARTITIONED AS (
        SELECT
            C.HACKER_ID,
            COUNT(C.CHALLENGE_ID) AS COUNT_CH,
            ROW_NUMBER() OVER (
                PARTITION BY COUNT(C.CHALLENGE_ID)
                ORDER BY
                    C.HACKER_ID
            ) AS ROWN
        FROM CHALLENGES C
        GROUP BY C.HACKER_ID
    )
SELECT
    H.HACKER_ID,
    H.NAME,
    P.COUNT_CH
FROM HACKERS H
    INNER JOIN PARTITIONED P ON H.HACKER_ID = P.HACKER_ID
WHERE (
        P.COUNT_CH = (
            SELECT
                MAX(COUNT_CH)
            FROM
                PARTITIONED
        )
        OR P.COUNT_CH NOT IN (
            SELECT COUNT_CH
            FROM PARTITIONED
            WHERE ROWN = 2
        )
    )
ORDER BY
    P.COUNT_CH DESC,
    H.HACKER_ID;