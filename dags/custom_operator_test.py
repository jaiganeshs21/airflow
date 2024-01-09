
from airflow import DAG
from datetime import datetime
from codebase.custom_operator import SampleExpressionEvaluateOperator, IfBlockOperator, ElseBlockOperator, ElifBlockOperator, ActionBlockOperator

default_args = {
    "owner": "everstage-workflow",
}
dag = DAG(
    "sample_test_dag",
    start_date=datetime.now(),
    default_args=default_args,
    schedule_interval=None,
)


experssion_eval = SampleExpressionEvaluateOperator(task_id='expression_evaluator', dag=dag)
if_block = IfBlockOperator(task_id='if_block', dag=dag)
elif_block = ElifBlockOperator(task_id='elif_block', dag=dag)
else_block = ElseBlockOperator(task_id='else_block', dag=dag)
action_blog = ActionBlockOperator(task_id='action_block', dag=dag)


# Define dependencies

experssion_eval >> if_block
experssion_eval >> elif_block
experssion_eval >> else_block

if_block >> action_blog
else_block >> action_blog
elif_block >> action_blog