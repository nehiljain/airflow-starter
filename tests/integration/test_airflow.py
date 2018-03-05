import os
from airflow.models import DagBag


def test_airflow_dagbag():
  dagbag = DagBag(os.getenv('AIRFLOW_HOME'))
  assert dagbag.size() > 0
  report = dagbag.dagbag_report()
  dag_id_list = ['demo_dag']
  for dag_id in dag_id_list:
    assert dag_id in report

