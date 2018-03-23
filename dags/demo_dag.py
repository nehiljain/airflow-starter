from __future__ import print_function
from builtins import range
import os
import sys
import airflow
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.models import DAG
import time
from pprint import pprint

DAG_ID = os.path.basename(__file__).replace(".pyc", "").replace(".py", "")
args = {
    'owner': 'nehiljain',
    'start_date': airflow.utils.dates.days_ago(2)
}

dag = DAG(
    dag_id=DAG_ID,
    default_args=args,
    schedule_interval='*/5 * * * *')


def print_context(ds, **kwargs):
    pprint(kwargs)
    print(ds)
    return 'Whatever you return gets printed in the logs'

stream1_task = PythonOperator(
    task_id='print_the_context_stream1',
    provide_context=True,
    op_kwargs={'stream': 1},
    python_callable=print_context,
    dag=dag)

stream2_task = PythonOperator(
    task_id='print_the_context_stream2',
    provide_context=True,
    op_kwargs={'stream': 2},
    python_callable=print_context,
    dag=dag)


start_task = DummyOperator(task_id='start_task',
                           dag=dag)

start_task.set_downstream([stream1_task, stream2_task])

