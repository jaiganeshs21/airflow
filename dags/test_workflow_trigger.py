from airflow import DAG
from dags.generate_dag import generate_dag

generated_dag: DAG = generate_dag("test_workflow_trigger")
