from __future__ import print_function
from builtins import range
import airflow
from airflow.operators.python_operator import PythonOperator
from airflow.models import DAG


import time
from pprint import pprint

args = {
    'owner': 'nehiljain',
    'start_date': airflow.utils.dates.days_ago(2)
}

dag = DAG(
    dag_id='demo_dag',
    default_args=args,
    schedule_interval=None)


def print_context(ds, **kwargs):
    pprint(kwargs)
    print(ds)
    return 'Whatever you return gets printed in the logs'

run_this = PythonOperator(
    task_id='print_the_context',
    provide_context=True,
    python_callable=print_context,
    dag=dag)


