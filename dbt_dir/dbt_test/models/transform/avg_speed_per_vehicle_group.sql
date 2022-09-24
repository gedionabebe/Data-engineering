with database_data as (
    select *
    from {{ source('test2', 'traffic') }}
),

t_data as (
    select
        v_type,
        AVG(speed)
    from database_data
    group by v_type
)
SELECT *
FROM t_data