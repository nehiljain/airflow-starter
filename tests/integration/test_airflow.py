import os
from airflow.models import DagBag


def test_airflow_dagbag():
  print(os.getenv('AIRFLOW_HOME'))
  dagbag = DagBag(os.getenv('AIRFLOW_HOME'))
  assert dagbag.size() > 0
  report = dagbag.dagbag_report()
  dag_id_list = ['demo_dag', 'db_cleanup_dag','distributaries_dag', 'source_sequential_dag', 'tributaries_dag']
  for dag_id in dag_id_list:
    assert dag_id in report

