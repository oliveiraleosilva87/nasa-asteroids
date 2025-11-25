import os
from datetime import datetime
from pathlib import Path
from src.custom_logger.logger import get_logger

logger = get_logger(__name__)

logger.info(f"Starting to run the Python script located in {os.path.abspath(__file__)}")

logger.info(f"Setting default files and directories to be used ...")
# place directories variables here

project_root = Path(__file__).resolve().parents[2].name
logger.info(f"Setting project root folder name to {project_root} ...")

logger.info("Defining functions to be used in the main logic ...")
# place main functions here

def main():
    # start market
    start_time = datetime.now()
    logger.info(f"Execution started at: {start_time.strftime("%Y-%m-%d %H:%M:%S")}")
    logger.info("=" * 50)
    logger.info(f"")
    logger.info(f"      Starting execution for {project_root}       ")
    logger.info("")
    logger.info("=" * 50)

    try:
        logger.info("       Running maincls logic of the code ...      ")
    
    except Exception as e:
        logger.error(f"An error occurred: {e}")
    
    finally:
        # finish marker
        logger.info("=" * 50)
        logger.info("")
        logger.info(f"      Finished execution for {project_root}       ")
        logger.info("")
        logger.info("=" * 50)
        end_time = datetime.now()
        logger.info(f"Execution finished at: {end_time.strftime("%Y-%m-%d %H:%M:%S")}")

        # log duration
        duration = end_time - start_time
        logger.info(f"Total execution time: {duration}")

    

if __name__ == "__main__":
    main()
