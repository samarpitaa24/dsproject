#below imports are copied from data_ingestion.py 
#1
import dataclasses
import os 
import sys #to hangle custom exception on logging
from src.dsproject.exception import CustomException
from src.dsproject.logger import logging
import pandas as pd

#2
from dotenv import load_dotenv
import pymysql 

load_dotenv() #loads all variables from env file

host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
db = os.getenv("db")

#3
def read_sql_data():
    logging.info("readinng sql database started")
    try:
        mydb = pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db
        )
        logging.info(f"Connection established with DB: {mydb}")

        df = pd.read_sql_query('Select * from student', mydb)
        print(df.head())
        
        return df
        
    except Exception as ex:
        raise CustomException(ex,sys)