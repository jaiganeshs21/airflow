from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from celery import app, shared_task
from celery import Celery

# from simple_dag import everstage_api_task

default_args = {
    "owner": "airflow",
    "start_date": datetime(2024, 1, 30),
}

dag = DAG(
    "api_testing",
    default_args=default_args,
    schedule_interval=timedelta(minutes=5),
)

@shared_task
def testing_addition():
    a = 50
    b = 20
    print("The sum of two number", a + b)


queue_name = "eq.BASIC.DATABOOK.1"

api_task = PythonOperator(
    task_id="task1",
    python_callable=testing_addition.si().set(queue=queue_name),
    queue=queue_name,
    dag=dag,
)

api_task



