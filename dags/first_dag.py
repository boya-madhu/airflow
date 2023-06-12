from airflow import DAG
from datetime import datetime,timedelta
from airflow.operators.python import PythonOperator

default_args={
    'owner':'madhu',
    'retries': 5,
    'retry_delay':timedelta(minutes=1)
}

def greetings(name,age):
    print(f"hii my name is {name} and my age is {age}")

with DAG(
    dag_id='first_dag',
    description='this is our first dag',
    default_args=default_args,
    start_date=datetime(2023,5,2,2),
    schedule_interval='@daily'

    
) as dag:
    task1 = PythonOperator(
        task_id='greetings',
        python_callable=greetings,
        op_args=('madhu',20)
    )
    task1