import os 
import logging 
import sys 

logging.basicConfig(
    level = logging.INFO,
    format = "%(message)s"
    filename = "pipeline.log"
)

if __name__ == "__main__":

    stepname = "step1"
    try:
        print(f"{stepname}")
        os.system("python script1.py")
        logging.info(f"{stepname} complete")
    else: 
        logging.info(f"{stepname} failed")
        sys.exit(f"{stepname} failed") 

    stepname = "step2"
    try:
        print(f"{stepname}")
        os.system("python script2.py")
        logging.info(f"{stepname} complete")
    else: 
        logging.info(f"{stepname} failed")
        sys.exit(f"{stepname} failed") 
