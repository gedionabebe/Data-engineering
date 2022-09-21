with database_data as (
    select *
    from {{ source('traffic_data', 'traffic') }}
),

t_data as (
    select
        v_type,
        AVG(traveled_d)
    from database_data
    group by v_type
)
SELECT *
FROM t_data