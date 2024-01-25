from datetime import datetime
from airflow.operators.python_operator import PythonOperator
from airflow import DAG

def print_dag_details(dag):
    print("inside_printing")
    for task_id, task in dag.task_dict.items():
        print(f"Task ID: {task_id}")
        print(f"Task Type: {type(task).__name__}")
        print(f"Upstream Task IDs: {[t.task_id for t in task.upstream_list]}")
        print(f"Downstream Task IDs: {[t.task_id for t in task.downstream_list]}")
        print("\n")


def test_function():
    print("Hello_JAI")


def generate_dag(workflow_id):
    """
    This function generates a DAG from a workflow definition
    """
    print("inside_generate_dag")
    parent_dag = DAG(
        dag_id=workflow_id,
        start_date=datetime(2024, 1, 23),
        default_args={"owner": "everstage_workflow"},
    )

    workflow_definition = {
        "nodes": [
            {"id": "1", "data": {"component": "WHEN"}},
            {"id": "2", "data": {"component": "IF"}},
            {"id": "4", "data": {"component": "THEN"}},
            {"id": "3", "data": {"component": "ELSE"}},
        ],
        "edges": [
            {"source": "2", "target": "3"},
            {"source": "1", "target": "2"},
            {"source": "2", "target": "4"},
        ],
        "start": "1",
    }

    node_id_to_operator = {}

    for node in workflow_definition["nodes"]:
        if node["data"]["component"] == "WHEN":
            operator = PythonOperator(
                task_id=node["id"],
                python_callable=test_function,
                dag=parent_dag,
            )
        elif node["data"]["component"] == "IF":
            operator = PythonOperator(
                task_id=node["id"],
                python_callable=test_function,
                dag=parent_dag,
            )
        elif node["data"]["component"] == "ELSE":
            operator = PythonOperator(
                task_id=node["id"],
                python_callable=test_function,
                dag=parent_dag,
            )
        elif node["data"]["component"] == "THEN":
            operator = PythonOperator(
                task_id=node["id"],
                python_callable=test_function,
                dag=parent_dag,
            )
        else:
            raise Exception("Invalid component type")

        node_id_to_operator[node["id"]] = operator

    for edge in workflow_definition["edges"]:
        source_node_id = edge["source"]
        target_node_id = edge["target"]
        source_operator = node_id_to_operator.get(source_node_id)
        target_operator = node_id_to_operator.get(target_node_id)

        if source_operator and target_operator:
            source_operator.set_downstream(target_operator)

    return parent_dag
