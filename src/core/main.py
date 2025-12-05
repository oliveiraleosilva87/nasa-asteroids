import os
from datetime import datetime
from pathlib import Path
import requests
from src.custom_logger.logger import get_logger

logger = get_logger(__name__)

logger.info(f"Starting to run the Python script located in {os.path.abspath(__file__)}")


logger.info(f"Setting default files and directories to be used ...")
# place directories variables here


project_root = Path(__file__).resolve().parents[2].name
logger.info(f"Setting project root folder name to {project_root} ...")


logger.info("Defining default variables and parameters to be used ...")
api_base_url = "https://api.nasa.gov/neo/rest/v1"


logger.info("Setting API parameters ...")
params = {"start_date": "2025-12-01", "end_date": "2025-12-05", "api_key": "DEMO_KEY"}


logger.info("Defining functions to be used in the main logic ...")


def get_feed_items():
    api_endpoint = "/feed"
    api_url = f"{api_base_url}{api_endpoint}"

    response = requests.get(api_url, params=params)
    if response.status_code == 200:
        feed_data = response.json()
        return feed_data
    else:
        logger.error(f"Failed to fetch data: {response.status_code}")
        return {}


def main():
    # start market
    start_time = datetime.now()
    logger.info(f"Execution started at: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
    logger.info("=" * 50)
    logger.info(f"")
    logger.info(f"      Starting execution for {project_root}       ")
    logger.info("")
    logger.info("=" * 50)

    try:

        logger.info("Fetching feed items from NASA NeoWs API ...")
        feed_data = get_feed_items()

        if feed_data:
            logger.info("Successfully fetched feed data from NASA NeoWs API !")

            # total fetched NEOs from feed
            neo_count = feed_data.get("element_count", 0)
            logger.info(f"Number of Near Earth Objects (NEOs) in the feed: {neo_count}")
        else:
            logger.warning("No data retrieved from the API.")

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
        logger.info(f"Execution finished at: {end_time.strftime('%Y-%m-%d %H:%M:%S')}")

        # log duration
        duration = end_time - start_time
        logger.info(f"Total execution time: {duration}")


if __name__ == "__main__":
    main()
