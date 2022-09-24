-- Use the `ref` function to select from other models

select *
from "test2"."traffic"."my_first_dbt_model"
where id = 1