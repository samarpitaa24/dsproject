import os #we need generic folder path
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO) #generic logging configuration

project_name= 'dsproject'

list_of_files = [
    # ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/components/model_monitoring.py",
    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/pipelines/training_pipeline.py",
    f"src/{project_name}/pipelines/prediction_pipeline.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/utils.py",
    "app.py",
    "Dockerfile",
    "requirements.txt", 
    "setup.py",
    "main.py"
    
    ]

for filepath in list_of_files:
    filepath = Path(filepath) #retrieves project ka relavtive path
    filedir , filename = os.path.split(filepath)
    
    if filedir!="": #if folder path is not empty 
        os.makedirs(filedir, exist_ok=True) #then create the path and if it already exists? then dont throw error 
        logging.info(f"Creating directory : {filedir} for the file {filename}") #Creating directory: project/data for the file input.txt

        
    if (not os.path.exists(filepath) or (os.path.getsize(filepath)==0)): #Check if file doesn't exist or is empty
        with open(filepath, 'w') as f: # This creates an empty file if it doesn’t already exist
            pass
        logging.info(f"creating empty file: {filepath}") #creating empty file: project/data/input.txt

        
    else: #(file already exists and is not empty)
        logging.info(f"{filename} already exists")
    
    
    """
                                       CODE TO AUTOMATE CREATION OF FOLDER STRUCTURE
    Explanation of code w example : 
    
     filepath = "project/data/input.txt"
     For "project/data/input.txt":
        filedir = "project/data"
        filename = "input.txt"
        
    Since filedir = "project/data", it's not empty
    So it creates the folder path project/data
    (exist_ok=True means no error if it already exists)
            Creating directory: project/data for the file input.txt

    NOTE : Run command -> python template.py
    NOTE : create env command : conda create -p venv python==3.9 -y
        conda activate venv\
        conda deactivate
    """
