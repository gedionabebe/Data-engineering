from datetime import  timedelta
import pandas as pd
import sys,os
import logging
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago
from airflow.utils.dates import timedelta

default_args = {
    "owner": "User",
    "retries": 1,
    "email": ["gedionandme@gmail.com"],
    "email_on_failaure": True,
    "retry_delay": timedelta(minutes=10),
}

dag = DAG(
    dag_id="create_table_and_fill_table",
    default_args=default_args,
    schedule_interval="@daily",
    start_date=days_ago(1),
    catchup=False,
    dagrun_timeout=timedelta(minutes=60),
    description="executing the sql scripts",
)

dbt_run_transfromations = BashOperator(
    task_id="dbt_run_transfromations", 
    bash_command="dbt run", 
    dag=dag)

dbt_gernerate_docs = BashOperator(
    task_id="dbt_gernerate_docs", 
    bash_command="dbt docs generate", 
    dag=dag)

dbt_serve_docs = BashOperator(
    task_id="dbt_gernerate_docs", 
    bash_command="dbt docs serve", 
    dag=dag)

dbt_run_transfromations >> dbt_gernerate_docs >> dbt_serve_docs