# from everstage.airflow import generate_dag
# from everstage.airflow import lookup_workflow_definition

# workflow_def = lookup_workflow_definition("fdsdf-adfad-fdasf-adfa")
# dag = generate_dag(workflow_def)


# #############################################

# def publish_workflow():
#     # write to postgres database
#     # write_dag_to_s3(uuid)


# def write_dag_to_s3(definition_id):
#     code_template = """
#     from everstage.airflow import generate_dag
#     from everstage.airflow import lookup_workflow_definition

#     workflow_def = lookup_workflow_definition({definition_id})
#     dag = generate_dag(workflow_def)
#     """

#     code = code_template.format(definition_id=definition_id)
#     write_to_s3(code, "dags/{}.py".format(definition_id))
#     return code


# # Placeholder for get_df function
# def get_df(datasheet_id):
#     # Assuming this function returns a DataFrame for demonstration purposes
#     return pd.DataFrame()


# def read_and_filter_data(context, column, value, block_id):
#     file_path = context["ti"].xcom_pull(
#         key="df_file_loc", task_ids="expression_evaluator"
#     )
#     data = pd.read_csv(file_path)
#     filtered_rows = data[data[column] == value]
#     if not filtered_rows.empty:
#         context["ti"].xcom_push(key="filtered_data", value=filtered_rows)
#         context["ti"].xcom_push(key="block_id", value=block_id)


# class DatasheetDataChangeOperator(BaseOperator):
#     @apply_defaults
#     def __init__(self, datasheet_id, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.datasheet_id = datasheet_id

#     def execute(self, context):
#         # if any file is written into ~/snapshot_data/{client_id}/{datasheet_id}/
#         # Ask DG - datasheet_snapshot_mapping -> datasheet_id -> file_location ?
#         # Use an airflow sensor to observe the above table and run after an entry is made in it
#         # Pass the file location to the next operator (xcom_push -> {file_location})
#         df = get_df(datasheet_id=self.datasheet_id)
#         file_path = "data.csv"
#         # data/workflow_id/datasheet_id/
#         df.to_csv(file_path, index=False)

#         context["ti"].xcom_push(key="df_file_loc", value=file_path)
