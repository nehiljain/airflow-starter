from __future__ import print_function
from builtins import range
import os
import sys

import airflow
from airflow.operators.dummy_operator import DummyOperator
from airflow.models import DAG

DAG_ID = os.path.basename(__file__).replace('.pyc', '').replace('.py', '')
args = {
    'owner': 'nehiljain',
    'start_date': airflow.utils.dates.days_ago(2)
}


dag = DAG(
    dag_id=DAG_ID,
    default_args=args,
    schedule_interval='*/5 * * * *')

a_task = DummyOperator(task_id='a', dag=dag)
b_task = DummyOperator(task_id='b', dag=dag)
c_task = DummyOperator(task_id='c', dag=dag)
d_task = DummyOperator(task_id='d', dag=dag)
e_task = DummyOperator(task_id='e', dag=dag)
f_task = DummyOperator(task_id='f', dag=dag)
g_task = DummyOperator(task_id='g', dag=dag)
h_task = DummyOperator(task_id='h', dag=dag)


a_task.set_downstream(b_task)
b_task.set_downstream([c_task, e_task, g_task])
c_task.set_downstream(d_task)
e_task.set_downstream(f_task)
g_task.set_downstream(h_task)


