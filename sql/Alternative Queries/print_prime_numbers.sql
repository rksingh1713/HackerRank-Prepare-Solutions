with recursive numbers(n) as (
        select 2
        union all
        select n + 1
        from numbers
        where
            n < 1000
    ),
    primes(p) as (
        select n
        from numbers n1
        where not exists(
                select 1
                from
                    numbers n2
                where
                    n2.n < n1.n
                    and n1.n mod n2.n = 0
            )
    )
select
    group_concat(p separator '&')
from primes;