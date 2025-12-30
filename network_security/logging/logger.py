import logging
import os
from datetime import datetime

LOG_FILENAME = f"{datetime.now().strftime('%d_%m_%y_%H_%M_%S')}.log"

log_dir= os.path.join(os.getcwd(),"logs")

os.makedirs(log_dir,exist_ok=True)

log_file_path = os.path.join(log_dir,LOG_FILENAME)

logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format="[%(asctime)s] -- %(lineno)d -- %(name)s -- %(levelname)s -- %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)