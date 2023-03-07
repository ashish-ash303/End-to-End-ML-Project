import logging # Used to track excution
import os
from datetime import datetime


LOG_File=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" #Creating the log file

logs_path=os.path.join(os.getcwd(),"logs",LOG_File) # Giving the location where it is saved

os.makedirs(logs_path,exist_ok=True) # Making the directory if it is already present append the log inside it.

LOG_FILE_PATH=os.path.join(logs_path,LOG_File) # Path of the log file

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    
)


if __name__=="__main__":
    logging.info("Logging Has Started")






