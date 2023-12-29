# making a custom log..

import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
# asci time for the timestamp
# levelname = level of the log
# module = from which module is the file being run?
# message = the message

log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log") # this is the path for the file that does the logging

os.makedirs(log_dir, exist_ok=True) # creating the directory for the log file

# the log logic:

logging.basicConfig(
    level = logging.INFO,
    format = logging_str,

    handlers = [
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("TextSummarizerLogger")

