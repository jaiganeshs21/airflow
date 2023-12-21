from airflow import DAG
from airflow.providers.apache.kafka.operators.kafka import KafkaConsumerOperator
from airflow.operators.email_operator import EmailOperator
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
import csv
import json

default_args = {
    'start_date': days_ago(1),
}

dag = DAG(
    'kafka_message_routing',
    default_args=default_args,
    description='A simple Kafka message routing DAG',
    schedule_interval=None,
)

def process_message(message):
    message = json.loads(message.value())
    if 'notification change' in message:
        return 'email', message
    elif 'datasheet data change' in message:
        return 'csv', message
    else:
        return 'unknown', message

consume = KafkaConsumerOperator(
    task_id='consume',
    topic='input_topic',
    kafka_conn_id='kafka_default',
    dag=dag,
)

def send_email(message):
    EmailOperator(
        task_id='send_email',
        to=message['email'],
        subject='Notification Change',
        html_content=message['content'],
        dag=dag,
    ).execute(context=None)

def write_to_csv(message):
    with open('data_changes.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(message['changes'])

process = PythonOperator(
    task_id='process',
    python_callable=process_message,
    op_args=[consume.output],
    dag=dag,
)

email = PythonOperator(
    task_id='email',
    python_callable=send_email,
    op_args=[process.output],
    dag=dag,
)

csv = PythonOperator(
    task_id='csv',
    python_callable=write_to_csv,
    op_args=[process.output],
    dag=dag,
)

consume >> process
process >> email
process >> csv