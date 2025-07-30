##database mysql--> read data --> data in train, test split format 

#1
import dataclasses
import os 
import sys #to hangle custom exception on logging
from src.dsproject.exception import CustomException
from src.dsproject.logger import logging
import pandas as pd

#7
from src.dsproject.utils import read_sql_data
from sklearn.model_selection import train_test_split

#2
from dataclasses import dataclass

#3
@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', 'train.csv') #want to save it inside artifact folder as train.csv
    test_data_path: str = os.path.join('artifacts', 'test.csv') 
    raw_data_path: str = os.path.join('artifacts', 'raw.csv') 

#4 -> 5 in utils
class DataIngestion:
    def __init__(self):
        self.ingestion_config= DataIngestionConfig() #now it'll create ingestion_config type folder having train, test, raw data paths
        
    def initiate_data_ingestion(self):
        #reading from sql dn
        try:
            ##reading data code 
            #6 <- after step 3 in utils
            df = read_sql_data()
            logging.info("Reading completed from MYsql database")
            
            ##all the data coming after reading, we've to save data in artifacts folder and 3 diff files
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True) #passing the curr folder path where train test files are to be created
            
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)  # Raw full data
            # Split the data
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            
            logging.info("Data Ingestion is completed")
            
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
            ## from here go to app.py to run this
            
                
            
        except Exception as e:
            raise CustomException(e,sys)
        
        