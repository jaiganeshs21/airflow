from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator


# from workflow_builder.dags.testing import test_func


# test_func()


# from commission_engine.accessors.databook_accessor import DatabookAccessor

# import commission_engine.accessors.databook_accessor as databook_accessor


def execute_workflow_condition(condition, **kwargs):
    a = kwargs.get("a", 0)



    
    if condition["Component"] == "IF":
        if eval(condition["Condition"]):
            return "Executing 'Then' branch"
        else:
            return "Executing 'Else' branch"
    elif condition["Component"] == "Action":
        return f"Executing Action: {condition['Msg']}"


def generate_dag(workflow_condition):
    default_args = {
        "owner": "airflow",
        "start_date": datetime(2023, 1, 1),
        "retries": 1,
    }

    dag = DAG(
        "dynamic_workflow_dag",
        default_args=default_args,
        description="A dynamic workflow DAG",
        schedule_interval=None,  # Set to None if you want to trigger the DAG manually
    )

    tasks = {}

    for condition in workflow_condition:
        if condition["Component"] == "IF":
            execute_task = PythonOperator(
                task_id=f"execute_condition_{condition['Id']}",
                python_callable=execute_workflow_condition,
                provide_context=True,
                op_args=[condition],
                dag=dag,
            )
        elif condition["Component"] == "Action":
            execute_task = PythonOperator(
                task_id=f"execute_action_{condition['Id']}",
                python_callable=execute_workflow_condition,
                provide_context=True,
                op_args=[condition],
                dag=dag,
            )

        tasks[condition["Id"]] = execute_task

        if "Then" in condition:
            tasks[condition["Then"]].set_upstream(execute_task)
        if "Else" in condition:
            tasks[condition["Else"]].set_upstream(execute_task)

    return dag


# tasks = {
#     1 : task_for_1,
#     2 : task_for_2,
#     3 : task_for_3
# }


def execute_dag(dag):
    dag.run()


# Case 1
workflow_condition_1 = [
    {"Id": 2, "Component": "Action", "Msg": "a is greater than 10"},
    {"Id": 3, "Component": "Action", "Msg": "a is less than 10"},
    {
        "Id": 1,
        "Component": "IF",
        "Condition": "a>10",
        "Then": 2,  # This indicates block with id 2 needs to be execute
        "Else": 3,  # This indicates block with id 3 needs to be execute
    },
]


# Case 2
workflow_condition_2 = [{"Component": "Action", "Msg": "Just an action", "Id": 1}]

# Case 3
workflow_condition_3 = [
    {"Id": 1, "Component": "Action", "Msg": "Just an action"},
    {"Id": 3, "Component": "Action", "Msg": "a is greater than 10"},
    {"Id": 4, "Component": "Action", "Msg": "a is less than 10"},
    {"Id": 2, "Component": "IF", "Condition": "a>10", "Then": 3, "Else": 4},
]

# Generate the DAG based on the workflow conditions
# generated_dag = generate_dag(workflow_condition_1)
# generated_dag_2 = generate_dag(workflow_condition_2)
generated_dag = generate_dag(workflow_condition_1)


execute_dag(generated_dag)

# print("generated_dag_1", generated_dag_1)


# for task_id, task in generated_dag_1.task_dict.items():
#     print(f"Task ID: {task_id}")
#     print(f"   Upstream tasks: {task.upstream_task_ids}")
#     print(f"   Downstream tasks: {task.downstream_task_ids}")
#     print("\n")
