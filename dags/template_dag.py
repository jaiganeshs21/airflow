import os


def write_dag_to_s3():
    definition_id = "test_workflow_trigger"
    code_template = """
from dags.generate_dag import generate_dag
generated_dag = generate_dag("{definition_id}")
"""

    code = code_template.format(definition_id=definition_id)
    write_to_local_folder(code, "{}.py".format(definition_id))


def print_dag_details(dag):
    print("inside_printing")
    for task_id, task in dag.task_dict.items():
        print(f"Task ID: {task_id}")
        print(f"Task Type: {type(task).__name__}")
        print(f"Upstream Task IDs: {[t.task_id for t in task.upstream_list]}")
        print(f"Downstream Task IDs: {[t.task_id for t in task.downstream_list]}")
        print("\n")


def write_to_local_folder(code, file_name, folder_path="."):
    try:
        full_path = os.path.join(folder_path, file_name)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)

        with open(full_path, "w") as file:
            file.write(code)

        print(f"Code successfully written to {full_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


write_dag_to_s3()
