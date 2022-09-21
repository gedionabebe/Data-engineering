from datetime import  timedelta
import pandas as pd
import sys,os
import logging
from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.utils.dates import days_ago

default_args = {
    "owner": "User",
    "retries": 1,
    "retry_delay": timedelta(minutes=10),
}

dag = DAG(
    dag_id="create_table_and_fill_table",
    default_args=default_args,
    schedule_interval="@daily",
    start_date=days_ago(1),
    dagrun_timeout=timedelta(minutes=60),
    description="executing the sql scripts",
)

create_table = PostgresOperator(
    sql="create_table.sql",
    task_id="createtable_task",
    postgres_conn_id="postgres_eng",
    dag=dag,
)
fill_table = PostgresOperator(
    sql="fill_table.sql",
    task_id="fill_table_task",
    postgres_conn_id="postgres_eng",
    dag=dag,
)

create_table >> fill_table