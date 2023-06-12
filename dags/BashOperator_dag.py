from airflow import DAG
from datetime import datetime,timedelta
from airflow.operators.bash import BashOperator

default_args={
    'owner':'madhu',
    'retries': 5,
    'retry_delay':timedelta(minutes=1)
}

with DAG(
    dag_id='BashOperator_dag',
    description='this is our first dag',
    default_args=default_args,
    start_date=datetime(2023,5,2,2),
    schedule_interval='@daily'
) as dag:
    task1 = BashOperator(
        task_id='first_task',
        bash_command='echo "hello this is the first task"'
    )
    task2 = BashOperator(
        task_id='second_task',
        bash_command='echo "hello this is second task"'
    )
    task3 = BashOperator(
        task_id='third_task',
        bash_command='echo "hello this is third task"'
    )
    task4 = BashOperator(
        task_id='fourth_task',
        bash_command='echo "hello this is fourth task"'
    )
    task1.set_downstream(task2)
    task1.set_downstream(task3)
    task4 << [task2,task3]