
  create view "test2"."traffic"."my_second_dbt_model__dbt_tmp" as (
    -- Use the `ref` function to select from other models

select *
from "test2"."traffic"."my_first_dbt_model"
where id = 1
  );