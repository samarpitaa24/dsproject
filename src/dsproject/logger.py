import logging
import os
from datetime import datetime
from typing_extensions import Format

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" #log file name - will be saved as month, day,year,hour,min,sec format w .log extension i.e log file is created
log_path= os.path.join(os.getcwd(),"logs",LOG_FILE) #log folder path for the above log file
os.makedirs(log_path, exist_ok=True) #now creating that folder path if it doesnt exist, if it exists then? skip creation

LOG_FILE_PATH = os.path.join(log_path,LOG_FILE) #creates entire log file path by joining log path with log_file

""" suppose : 
    os.getcwd() → "C:/Users/Sam/myproject"
    LOG_FILE = "app.log"
    then log_path = "C:/Users/Sam/myproject/logs/app.log"
    
    You're telling Python:
    "I want to store my logs in a logs folder inside my project, and the log file name is whatever LOG_FILE is."
"""

#structure of log records inside log file
logging.basicConfig(
    filename=LOG_FILE_PATH, #within this file
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s -%(message)s", #defining format of log msg 
    level=logging.INFO, #there are diff levels like info, error for above format shown in msg
)   
"""
[2025-07-29 16:00:01] 42 mymodule - INFO - Successfully loaded the model.
lineno - line number
name - name of logger
acstime - timestamp of log creatin
logname - displays log level
"""