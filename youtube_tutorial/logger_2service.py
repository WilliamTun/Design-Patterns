
# logging service make it easier to:
#  1. visualise logs
#  2. search logs
#  3. more control over how long the logs are saved

# disadvantage
# 1. assume logging services are not secure
#    so do not log secrets / passwords / contact info 
# 2. know where log data is sent to and how long the data is stored. 
#    logging services are suppose to do the above for us
#    ...though mistakes can happen with 3rd parties

# A recommended logging service: PAPERTRAIL

import logging 
from logging.handlers import SysLogHandler 

PAPERTRAIL_HOST = "xxx.papertrailapp.com"
PAPERTRAIL_PORT = 12345

def main() -> None: 
    logger = logging.getLogger("willsLogs")
    logger.setLevel(logging.DEBUG)

    # allows us to send logs to service - and go to webbase interface to browse & search logs
    handler = SysLogHandler(address=(PAPERTRAIL_HOST, PAPERTRAIL_PORT)) 
    logger.addHandler(handler)

    logger.debug("debug msg")

if __name__ == "__main__":
    main()

