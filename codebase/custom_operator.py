import random
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults
import pandas as pd

class SampleExpressionEvaluateOperator(BaseOperator):
    @apply_defaults
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def execute(self, context):
        data = pd.DataFrame({
            "a": [random.randint(0, 100) for _ in range(20)],
            "b": [random.randint(0, 100) for _ in range(20)],
            "c": [random.randint(0, 100) for _ in range(20)],
            "blockA": [random.randint(0, 1) for _ in range(20)],
            "blockB": [random.randint(0, 1) for _ in range(20)],
            "blockC": [random.randint(0, 1) for _ in range(20)],
        })

        file_path = 'data.csv'
        try:
            data.to_csv(file_path, index=False)
        except Exception as e:
            print(f"An error occurred: {e}")

        context["ti"].xcom_push(key="df_file_loc", value=file_path)


class IfBlockOperator(BaseOperator):
    @apply_defaults
    def __init__(self, *args, **kwargs):
        super(IfBlockOperator, self).__init__(*args, **kwargs)

    def execute(self, context):
        file_path = context["ti"].xcom_pull(key="df_file_loc", task_ids="expression_evaluator")
        data = pd.read_csv(file_path)
        filtered_rows = data[data["blockA"] == 1]
        if not filtered_rows.empty:
            context["ti"].xcom_push(key="filtered_data", value=filtered_rows)


class ElifBlockOperator(BaseOperator):
    @apply_defaults
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def execute(self, context):
        file_path = context["ti"].xcom_pull(key="df_file_loc", task_ids="expression_evaluator")
        data = pd.read_csv(file_path)
        filtered_rows = data[data["blockB"] == 1]
        if not filtered_rows.empty:
            context["ti"].xcom_push(key="filtered_data", value=filtered_rows)


class ElseBlockOperator(BaseOperator):
    @apply_defaults
    def __init__(self, *args, **kwargs):
        super(ElseBlockOperator, self).__init__(*args, **kwargs)

    def execute(self, context):
        file_path = context["ti"].xcom_pull(key="df_file_loc", task_ids="expression_evaluator")
        data = pd.read_csv(file_path)
        filtered_rows = data[data["blockC"] == 1]
        if not filtered_rows.empty:
            context["ti"].xcom_push(key="filtered_data", value=filtered_rows)


class ActionBlockOperator(BaseOperator):
    @apply_defaults
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def execute(self, context):
        filtered_data = context["ti"].xcom_pull(key="filtered_data", task_ids=["if_block_operator", "elif_block_operator", "else_block_operator"])
        print("Filtered data:")
        print(filtered_data)