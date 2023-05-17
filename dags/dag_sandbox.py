from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

def print_hello():
    return "Hello, world!"

dag = DAG(
    "my_dag",
    default_args=default_args,
    description="A simple DAG to test Airflow",
    schedule_interval=timedelta(days=1),
    start_date=datetime(2023, 5, 17),
    catchup=False,
)

start_task = DummyOperator(task_id="start_task", dag=dag)
hello_task = PythonOperator(task_id="hello_task", python_callable=print_hello, dag=dag)
end_task = DummyOperator(task_id="end_task", dag=dag)

start_task >> hello_task >> end_task
