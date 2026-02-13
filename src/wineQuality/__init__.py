import os
import sys
import logging #to define custom logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]" #time&date : level: which module : what error

log_dir = "logs"

log_filepath = os.path.join(log_dir, "running_log.log")
os.makedirs(log_dir,exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
    )

logger = logging.getLogger("MLprojectlogger") #logger object 