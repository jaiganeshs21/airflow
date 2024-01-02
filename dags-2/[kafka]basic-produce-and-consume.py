from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from kafka import KafkaProducer, KafkaConsumer
from datetime import datetime

def produce_message():
    producer = KafkaProducer(bootstrap_servers='kafka:9092')
    producer.send('test-topic', b'Some Message')
    producer.flush()

def consume_message():
    consumer = KafkaConsumer('test-topic',
                             bootstrap_servers='kafka:9092',
                             auto_offset_reset='earliest')
    for message in consumer:
        print('consumed message',message.value)
        break

default_args = {
    'start_date': datetime(2022, 1, 1),
}

dag = DAG('kafka_dag', default_args=default_args, schedule_interval=None)

produce_task = PythonOperator(
    task_id='produce',
    python_callable=produce_message,
    dag=dag,
)

consume_task = PythonOperator(
    task_id='consume',
    python_callable=consume_message,
    dag=dag,
)

produce_task >> consume_task