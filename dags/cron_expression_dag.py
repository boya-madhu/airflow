from datetime import datetime,timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args={
    'owner':'madhu',
    'retries': 5,
    'retry_delay':timedelta(minutes=1)
}

with DAG(
    dag_id='cron_dag',
    default_args=default_args,
    start_date=datetime(2023,6,10,6,24),
    schedule_interval='53 6 * * *'
) as dag:
    task1 = BashOperator(
        task_id='first_task',
        bash_command='echo "this is the cron bash command"'
    )
    task1
