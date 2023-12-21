from kafka import KafkaProducer, KafkaConsumer
import json
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

# Kafka Producer
def producer_task():
    producer = KafkaProducer(bootstrap_servers='kafka:9092',
                             value_serializer=lambda v: json.dumps(v).encode('utf-8'))

    data = {"tag": "datasheet data changes", "1": "2", "2" : "3"}  # replace with your data
    
    #send data to topic
    if data.get('tag') == 'datasheet_data_changes':
        producer.send('datasheet-data-changes', data)
    elif data.get('tag') == 'datasheet_config_changes':
        producer.send('datasheet-config-changes', data)
    
    producer.flush()

# Kafka Consumer
def consumer_task():
    consumer = KafkaConsumer('datasheet-data-changes',
                             bootstrap_servers=['kafka:9092'],
                             auto_offset_reset='earliest',  # add this line
                             value_deserializer=lambda m: json.loads(m.decode('utf-8')))

    print('airflow123 Waiting for messages. Subscribed to:', consumer.subscription())
    for message in consumer:
        print('consumed message', message.value)
        break

# Apache Airflow
default_args = {
    'start_date': datetime(2022, 1, 1)
}

dag = DAG('kafka_csv', default_args=default_args, schedule_interval=None)

producer_operator = PythonOperator(task_id='producer_task', python_callable=producer_task, dag=dag)
consumer_operator = PythonOperator(task_id='consumer_task', python_callable=consumer_task, dag=dag)

producer_operator >> consumer_operator