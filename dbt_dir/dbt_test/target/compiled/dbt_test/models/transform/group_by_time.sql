with database_data as (
    select *
    from "test2"."public"."traffic"
),

t_data as (
    select 
        d_time,
        COUNT(*)
    from database_data
    group by d_time
)
SELECT *
FROM t_data