import logging
import os
from datetime import datetime
class Logs():
    def __init__(self):
        pass
    def logs():
            # Define the directory path where logs will be stored
            # log_directory = r"C:\Github\GetPassRuckus\Logs"
            log_directory = r"C:/Github/PowerBiAutomation/Logs"
                # Create the log directory if it doesn't exist
            if not os.path.exists(log_directory):
                    os.makedirs(log_directory)

                # Get the current date and time
            current_datetime = datetime.now()

                    # Generate a filename based on the current date within the log folder
            log_filename = os.path.join(log_directory, current_datetime.strftime("%Y-%m-%d") + "_log.log")

                    # Configure logging to output to this filename
            logging.basicConfig(
                level=logging.INFO,
                format="%(asctime)s %(levelname)s %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S",
                encoding= "utf-8",
                filename=log_filename  # Use the generated filename within the log folder
            )