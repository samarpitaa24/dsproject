from src.dsproject.logger import logging
from src.dsproject.exception import CustomException
import sys

from src.dsproject.components.data_ingestion import DataIngestion, DataIngestionConfig

if __name__=="__main__":
    logging.info("The execution has started")
    
    """_summary_
    this way when we expect an exception, we handle it, provide detailed msg of error and store its log in log folder
    """
    try:
        ## after step 6 in data_ingestion.py 
        ##step 1 <- after step 6 in d_i.py
        
        # data_ingestion_config = DataIngestionConfig() -> dont write since dataIngestionConfig will be called within dataIngestion
        data_ingestion = DataIngestion() 
        data_ingestion.initiate_data_ingestion()
        
    except Exception as e:
        logging.info("Custom exception") 
        raise CustomException(e,sys)