from airflow import DAG
from datetime import datetime
from codebase.custom_operator import SampleExpressionEvaluateOperator, IfBlockOperator, ElseBlockOperator, ActionBlockOperator
from codebase.hardcoded_testcase import get_test_case


def generate_dag(test_case):
    default_args = {
        "owner": "everstage-workflow",
    }

    dag = DAG(
        "sample_test_dag",
        start_date=datetime.now(),
        default_args=default_args,
        schedule_interval=None,
    )

    node_id_to_operator = {}

    for node in test_case["nodes"]:
        operator = None
        if node["data"]["component"] == "WHEN":
            operator = SampleExpressionEvaluateOperator(
                task_id=f"task_{node['id']}",
                dag=dag
            )
        elif node["data"]["component"] == "IF":
            operator = IfBlockOperator(
                task_id=f"task_{node['id']}",
                dag=dag
            )
        elif node["data"]["component"] == "ELSE":
            operator = ElseBlockOperator(
                task_id=f"task_{node['id']}",
                dag=dag
            )
        elif node["data"]["component"] == "THEN":
            operator = ActionBlockOperator(
                task_id=f"task_{node['id']}",
                dag=dag
            )

        node_id_to_operator[node["id"]] = operator

    for edge in test_case["edges"]:
        source_node_id = edge["source"]
        target_node_id = edge["target"]
        source_operator = node_id_to_operator.get(source_node_id)
        target_operator = node_id_to_operator.get(target_node_id)

        if source_operator and target_operator:
            source_operator >> target_operator

    return dag



test_case = get_test_case()
generated_dag = generate_dag(test_case)

for task in generated_dag.tasks:
    upstream_tasks = task.upstream_list
    downstream_tasks = task.downstream_list

    print(f"Upstream tasks for {task.task_id}: {[t.task_id for t in upstream_tasks]}")
    print(f"Downstream tasks for {task.task_id}: {[t.task_id for t in downstream_tasks]}")
    print("\n")