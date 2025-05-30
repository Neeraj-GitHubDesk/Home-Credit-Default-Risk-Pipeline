import os
import sys
from pymongo import MongoClient
import gridfs
from dotenv import load_dotenv

from src.utils.logger import get_logger
from src.utils.exception import CustomException

logger = get_logger(__name__, "data_ingestion.log")

class DataIngestion:
    def __init__(self):
        load_dotenv()
        self.mongo_uri = os.getenv("MONGO_URI")
        self.database_name = os.getenv("MONGO_DB")
        self.download_dir = "data/raw"
        self.zip_filename = "dataset.zip"  # Name you used in upload; change if needed

        if not self.mongo_uri or not self.database_name:
            raise CustomException("MongoDB URI or DB name not set in environment variables.", sys)

    def download_zip_from_mongo(self):
        try:
            os.makedirs(self.download_dir, exist_ok=True)
            logger.info(f"Connecting to MongoDB at {self.mongo_uri}, DB: {self.database_name}")

            client = MongoClient(self.mongo_uri)
            try:
                db = client[self.database_name]
                fs = gridfs.GridFS(db)

                logger.info(f"Looking for file '{self.zip_filename}' in GridFS...")
                file_data = fs.find_one({"filename": self.zip_filename})

                if not file_data:
                    raise CustomException(f"File '{self.zip_filename}' not found in MongoDB GridFS.", sys)

                local_path = os.path.join(self.download_dir, self.zip_filename)
                logger.info(f"Downloading and saving to {local_path} ...")

                with open(local_path, "wb") as f:
                    f.write(file_data.read())

                logger.info(f"Download successful. File saved at {local_path}")
                return local_path

            finally:
                client.close()

        except Exception as e:
            logger.error(f"Error during data ingestion: {e}")
            raise CustomException(e, sys)


if __name__ == "__main__":
    ingestion = DataIngestion()
    ingestion.download_zip_from_mongo()