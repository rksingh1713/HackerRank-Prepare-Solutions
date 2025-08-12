SELECT
    A.SUBMISSION_DATE,
    A.NUM_UNIQUE,
    A.HACKER_ID,
    H.NAME
FROM (
        SELECT
            S.SUBMISSION_DATE, (
                SELECT
                    COUNT(DISTINCT S1.HACKER_ID)
                FROM
                    SUBMISSIONS AS S1
                WHERE
                    S1.SUBMISSION_DATE = S.SUBMISSION_DATE
                    AND (
                        SELECT
                            COUNT(DISTINCT S2.SUBMISSION_DATE)
                        FROM
                            SUBMISSIONS AS S2
                        WHERE
                            S2.SUBMISSION_DATE < S1.SUBMISSION_DATE
                            AND S2.HACKER_ID = S1.HACKER_ID
                    ) = DATEDIFF(
                        S.SUBMISSION_DATE, (
                            SELECT
                                MIN(S3.SUBMISSION_DATE)
                            FROM
                                SUBMISSIONS AS S3
                        )
                    )
            ) AS NUM_UNIQUE, (
                SELECT
                    S4.HACKER_ID
                FROM
                    SUBMISSIONS AS S4
                WHERE
                    S4.SUBMISSION_DATE = S.SUBMISSION_DATE
                GROUP BY
                    S4.HACKER_ID
                ORDER BY
                    COUNT(*) DESC,
                    S4.HACKER_ID
                LIMIT
                    1
            ) AS HACKER_ID
        FROM (
                SELECT
                    DISTINCT A.SUBMISSION_DATE
                FROM
                    SUBMISSIONS AS A
            ) AS S
    ) AS A
    JOIN HACKERS AS H ON A.HACKER_ID = H.HACKER_ID
ORDER BY A.SUBMISSION_DATE