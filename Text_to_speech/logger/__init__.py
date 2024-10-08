import logging 
import os
from datetime import datetime

##create log firectory

LOG_DIR = "pylogs"
LOG_DIR_PATH = os.path.join(os.getcwd(), LOG_DIR)

# create log directory using os.makedirs
os.makedirs(LOG_DIR,exist_ok=True)

#create logfile name
CURRENT_TIME_STAMP = F"{datetime.now().strftime('%y-%m-%d %H:%M:%S')}"
file_name=f"log_{CURRENT_TIME_STAMP}"
log_file_path = os.path.join(LOG_DIR,file_name)

# configure logging
logging.basicConfig(level=logging.INFO,
                    filename=log_file_path,
                    format="%(asctime)s %(levelname)s %(module)s ============>%(message)s",
                    datefmt= "%d-%m-%Y %H:%M")
                
# create object for logging
logger = logging.getLogger()