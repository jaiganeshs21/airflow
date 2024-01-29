# Orchestration with Apache Airflow

For effective orchestration, we rely on Apache Airflow.

All business logic should be implemented within the "everstage-spm/interstage-project/airflow" repository. Make a REST API call to execute the business logic.

Avoid integrating any business logic directly into this repository.

## Docker Build Command

To construct the Docker images, execute the following command:

```bash
docker-compose -f docker-compose-local-dev-live.yml up --build --remove-orphans

URL: localhost:8080

Default credentials:

Username: airflow
Password: airflow
