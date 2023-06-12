from airflow.decorators import dag,task
from datetime import datetime,timedelta

default_args={
    'owner':'madhu',
    'retries': 5,
    'retry_delay':timedelta(minutes=1)
}

@dag('api_dag',default_args=default_args,start_date=datetime(2023,2,3,5),schedule_interval='@daily')
def hello_world():
    
    @task()
    def get_name():
        return "madhu"
    
    @task()
    def get_age():
        return 20
    
    @task()
    def greet(name,age):
        print(f"hai my name is {name} and my age is {age}")

    name=get_name()
    age=get_age()

    greet(name,age)

greet_dag=hello_world()

