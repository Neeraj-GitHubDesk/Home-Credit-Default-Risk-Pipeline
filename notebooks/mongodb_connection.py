import os
import sys
from pymongo import MongoClient
import gridfs
from dotenv import load_dotenv

from src.utils.logger import get_logger
from src.utils.exception import CustomException

# Logger setup
logger = get_logger(__name__, "upload_to_mongo.log")

def upload_zip_to_mongo(zip_file_path: str):
    try:
        # Load credentials
        load_dotenv()
        mongo_uri = os.getenv("MONGO_URI")
        database_name = os.getenv("MONGO_DB")

        logger.info(f"Connecting to MongoDB at {mongo_uri}, DB: {database_name}")

        client = MongoClient(mongo_uri)
        db = client[database_name]
        fs = gridfs.GridFS(db)

        # Upload file
        logger.info(f"Uploading file: {zip_file_path}")

        with open(zip_file_path, "rb") as f:
            file_id = fs.put(f, filename=os.path.basename(zip_file_path))

        logger.info(f"Upload successful! GridFS file ID: {file_id}")

    except Exception as e:
        logger.error("Failed to upload dataset to MongoDB.")
        raise CustomException(e, sys)

# Example usage
if __name__ == "__main__":
    zip_path = os.path.abspath(os.path.join(os.getcwd(), "data", "dataset.zip"))
    upload_zip_to_mongo(zip_path)