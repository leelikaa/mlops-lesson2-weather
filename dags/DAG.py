from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from dotenv import load_dotenv

import os

from weather import weather_data_update

load_dotenv("/app/.env")
api_key = os.getenv("API_KEY")
city = "Moscow"

default_args={
        'owner':'airflow',
        'depends_on_past': False,
        'start_date': datetime(2024, 6, 15),
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 1,
        'retry_delay': timedelta(minutes=1),
    }

dag = DAG(
    'hw_MLops_e-kozlova-1_weather_data',
    default_args = default_args,
    description='Moscow weather info',
    schedule_interval=timedelta(minutes=1),
)

weather_update = PythonOperator(
    task_id='weather_data_update',
    python_callable= weather_data_update,
    op_args=['/app/weather.csv'],
    dag=dag)

weather_update
