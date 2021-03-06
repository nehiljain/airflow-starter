import os
from datetime import datetime

from freezegun import freeze_time
from airflow.models import DagBag


def test_airflow_dagbag():
    dagbag = DagBag(os.getenv('AIRFLOW_HOME'))
    assert dagbag.size() > 0
    report = dagbag.dagbag_report()
    dag_id_list = ['demo_dag', 'db_cleanup_dag', 'distributaries_dag',
                   'source_sequential_dag', 'tributaries_dag']
    for dag_id in dag_id_list:
        assert dag_id in report


def test_dynamic_start_date():
    """
    Tests that start date for dags are set 
    relative to instantiation date not a fixed date.
    """
    start_dates = {}
    freezer = freeze_time('2200-02-20')
    freezer.start()
    dagbag = DagBag(os.getenv('AIRFLOW_HOME'))
    for dag in dagbag.dags.values():
        dag_start_date = dagbag.get_dag(
            dag.dag_id).default_args.get('start_date')
        start_dates[dag.dag_id] = dag_start_date
    freezer.stop()

    time_insensitive_dags = ['']
    time_dependent_dags = ['']

    freezer = freeze_time('2300-02-20')
    freezer.start()
    dagbag = DagBag(os.getenv('AIRFLOW_HOME'))
    for dag in dagbag.dags.values():
        import pdb
        pdb.set_trace()
        dag_start_date = dagbag.get_dag(
            dag.dag_id).default_args.get('start_date')
        assert start_dates[dag.dag_id] != dag_start_date
    freezer.stop()
