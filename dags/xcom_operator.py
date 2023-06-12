from airflow import DAG
from datetime import timedelta,datetime
from airflow.operators.python import PythonOperator


default_args={
    'owner':'madhu',
    'retries': 5,
    'retry_delay':timedelta(minutes=5)
}

def greet(ti):
    firstname=ti.xcom_pull(task_ids='get_name', key='firstname')
    secondname=ti.xcom_pull(task_ids='get_name', key='secondname')
    age=ti.xcom_pull(task_ids='get_age',key='age')

    print(f"hi my name is {firstname} {secondname} and my age is {age}")

def get_name(ti):
    ti.xcom_push(key='firstname', value='madhu')
    ti.xcom_push(key='secondname', value='sab')

def get_age(ti):
    ti.xcom_push(key='age', value=20)

with DAG(
    'xcom_operator_with_function',
    description='this is our python_operator_dag',
    default_args=default_args,
    start_date=datetime(2023,5,2,2),
    schedule_interval='@daily'
) as dag:
    task1 = PythonOperator(
        task_id='greet',
        python_callable=greet,
        #op_kwargs={'age':20}
    )
    
    task2 = PythonOperator(
        task_id='get_name',
        python_callable=get_name
    )
    task3 = PythonOperator(
        task_id='get_age',
        python_callable=get_age
    )
    [task2,task3] >> task1