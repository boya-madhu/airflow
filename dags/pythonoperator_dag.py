from airflow import DAG
from datetime import timedelta,datetime
from airflow.operators.python import PythonOperator


default_args={
    'owner':'madhu',
    'retries': 5,
    'retry_delay':timedelta(minutes=5)
}

def fetch_data():
    print("data is being fetched")

def read_data():
    print("data is being readed")

def modify_data():
    print("data is being modified")

def update_data():
    print("data is being updated")

with DAG(
    'python_operator_with_function',
    description='this is our python_operator_dag',
    default_args=default_args,
    start_date=datetime(2023,5,2,2),
    schedule_interval='@daily'

    
) as dag:
    task1 = PythonOperator(
        task_id='fetch_data',
        python_callable=fetch_data
    )
    task2 = PythonOperator(
        task_id='read_data',
        python_callable=read_data
    )
    task3 = PythonOperator(
        task_id='modify_data',
        python_callable=modify_data
    )
    task4 = PythonOperator(
        task_id='update_data',
        python_callable=update_data
    )
    task1 >> task2 >> task3 >> task4