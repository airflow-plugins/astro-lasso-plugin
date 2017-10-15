from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from bson import ObjectId
# Custom Plugin
from airflow.operators import PutSchemaOperator

args = {
    'owner': 'andy.cooper',
    'start_date': datetime(2017, 10, 1, 0, 0),
    'provide_context': True
}

dag = DAG(
    'astro-lass-demo',
    schedule_interval="@once",
    default_args=args
)

start = DummyOperator(
    task_id='start_pipeline',
    dag=dag
)

put_schema = PutSchemaOperator(
    task_id='put_schema_operator',
    src_sys='salesforceBulk',
    src_tbl='leads',
    src_col='firstName',
    dst_sys='postgres', 
    dst_tbl='dim_leads', 
    dst_col='first_name',
    dag=dag
)

end = DummyOperator(
    task_id='end_pipeline',
    dag=dag
)

start.set_downstream(put_schema)
put_schema.set_downstream(end)
