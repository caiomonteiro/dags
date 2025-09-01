from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

# Definição básica da DAG
with DAG(
    dag_id="dag_teste",
    start_date=datetime(2025, 1, 1),
    schedule_interval="@daily",  # executa todo dia
    catchup=False,
    tags=["teste"],
) as dag:

    tarefa_1 = BashOperator(
        task_id="hello_airflow",
        bash_command="echo 'Hello Airflow! DAG sincronizada com sucesso 🚀'"
    )

    tarefa_1
