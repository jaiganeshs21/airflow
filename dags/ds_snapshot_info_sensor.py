from airflow import DAG
from airflow.providers.snowflake.hooks.snowflake import SnowflakeHook
from airflow.sensors.sql import SqlSensor
from datetime import datetime, timedelta

default_args = {
    "owner": "airflow_ever",
    "start_date": datetime(2024, 1, 22),
}

dag = DAG(
    "snowflake_monitoring_dag_1",
    default_args=default_args,
    description="A DAG to monitor changes in Snowflake table",
)

monitored_table = "DS_SNAPSHOT_INFO"


def snowflake_connection_test():
    try:
        hook = SnowflakeHook(snowflake_conn_id="local_snowflake")
        sql = f"SELECT COUNT(*) FROM {monitored_table}"
        hook.run(sql)
        records = hook.get_records(sql)
        print(f"Records: {records}")
    except Exception as e:
        print(f"Failed to connect to the database or execute query. Error: {e}")


snowflake_test = SqlSensor(
    task_id="snowflake_test_1",
    conn_id="local_snowflake",
    sql=f"SELECT COUNT(*) FROM {monitored_table}",
    mode="poke",
    timeout=60 * 5,  # timeout = 5 minutes
    poke_interval=30,  # check every 30 seconds
    dag=dag,
)

snowflake_test
