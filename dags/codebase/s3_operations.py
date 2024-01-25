import boto3


def write_to_s3(content, key, bucket_name="airflow-dags-local"):
    s3 = boto3.resource("s3")
    bucket = s3.Bucket(bucket_name)
    bucket.put_object(Key=key, Body=content)


def write_dag_to_s3(definition_id, bucket_name="airflow-dags-local"):
    code_template = """
    from everstage.airflow import generate_dag
    from everstage.airflow import lookup_workflow_definition

    workflow_def = lookup_workflow_definition({definition_id})
    dag = generate_dag(workflow_def)
    """

    code = code_template.format(definition_id=definition_id)
    write_to_s3(code, "dags/{}.py".format(definition_id), bucket_name)
    return code
