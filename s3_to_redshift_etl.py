from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='s3_to_redshift_etl',
    default_args=default_args,
    description='Load data from S3 into Redshift fact_sales table',
    schedule_interval=None,  # You can change this to a cron if you want it scheduled
    start_date=datetime(2023, 1, 1),
    catchup=False,
    tags=['etl', 'redshift'],
) as dag:

    load_fact_sales = PostgresOperator(
        task_id='load_fact_sales',
        postgres_conn_id='redshift_conn',
        sql="""
            COPY public.fact_sales
            FROM 's3://retailmart-data-warehouse/sales.csv'
            IAM_ROLE 'arn:aws:iam::151707281278:role/RedshiftS3CopyRole'
            FORMAT AS CSV
            IGNOREHEADER 1;
        """,
        database='retail_dw',  # Optional: only needed in Airflow 2.6+
    )

    load_fact_sales
