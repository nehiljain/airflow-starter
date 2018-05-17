import sys

import math
print('Python Version {}'.format(sys.version_info))
print('Math ceil function is built in: {} and returns {}'.format(
    math.ceil, type(math.ceil(3.6))))

from airflow.models import DAG

print('Math ceil function is overridden {} and returns {}'.format(math.ceil, type(math.ceil(3.6))))



