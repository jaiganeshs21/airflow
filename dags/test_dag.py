from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python_operator import PythonOperator

def execute():
    from ev_workflow.base import test_func
    # from spm.workflows import Workflow
    # Workflow.get(1).get_if_block()
    test_func()
    print("Whoa this works ?")

default_args = {
    'owner': 'everstage-workflow',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    default_args=default_args,
    dag_id="test_dag",
    start_date=datetime(2021, 11, 1),
    schedule_interval=None
) as dag:
    task1 = PythonOperator(
        task_id='task1',
        python_callable=execute
    )
    task1