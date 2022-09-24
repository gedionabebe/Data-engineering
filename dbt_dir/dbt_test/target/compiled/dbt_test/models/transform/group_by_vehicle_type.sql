with database_data as (
    select *
    from "test2"."public"."traffic"
),

t_data as (
    select 
        v_type,
        COUNT(*)
    from database_data
    group by v_type
)
SELECT *
FROM t_data