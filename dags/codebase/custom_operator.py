from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults


class EverstagExpressionevaluator(BaseOperator):
    @apply_defaults
    def __init__(self, expression, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.expression = expression

    def execute(self, context):
        dataset = context["ti"].xcom_pull(
            key=f"datasheet_data_efs_location_{self.dag_id}"
        )
        result_df = ever_expression_eval(dataset=dataset, expression=self.expression)

        file_path = f"expression_eval_{self.dag_id}.csv"
        result_df.to_csv(file_path, index=False)

        context["ti"].xcom_push(key=f"expression_eval_{self.dag_id}", value=file_path)


class IfBlockOperator(BaseOperator):
    @apply_defaults
    def __init__(self, *args, **kwargs):
        super(IfBlockOperator, self).__init__(*args, **kwargs)

    def execute(self, context):
        print("Inside If block", self.task_id)


class ElseBlockOperator(BaseOperator):
    @apply_defaults
    def __init__(self, *args, **kwargs):
        super(ElseBlockOperator, self).__init__(*args, **kwargs)

    def execute(self):
        print("Inside else block", self.task_id)


class ActionBlockOperator(BaseOperator):
    @apply_defaults
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def execute(self, context):
        data = context["ti"].xcom_pull(f"expression_eval_{self.dag_id}")
        print("data-action block", data)
        print("Inside Action block", self.task_id)


class DatasheetDataChangeOperator(BaseOperator):
    @apply_defaults
    def __init__(self, databook_id, client_id, datasheet_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.datasheet_id = datasheet_id
        self.databook_id = databook_id
        self.client_id = client_id

    def execute(self, context):
        datasheet_data_efs_location = get_datasheet_data_efs_file_location(
            datasheet_id=self.datasheet_id,
            databook_id=self.databook_id,
            client_id=self.client_id,
        )
        context["ti"].xcom_push(
            key=f"datasheet_data_efs_location_{self.dag_id}",
            value=datasheet_data_efs_location,
        )


def ever_expression_eval(dataset, expression):
    return dataset


def get_datasheet_data_efs_file_location(client_id, datasheet_id, databook_id):
    return "data.csv"
