import os
import sys
import zipfile
import shutil

from src.utils.logger import get_logger
from src.utils.exception import CustomException

logger = get_logger(__name__, "training_test_split.log")


class TrainingTestSplit:
    def __init__(self):
        self.raw_zip_path = os.path.join("data", "raw", "dataset.zip")
        self.processed_dir = os.path.join("data", "processed")
        self.temp_extract_dir = os.path.join("data", "temp_unzip")

        self.train_file_original = "application_train.csv"
        self.test_file_original = "application_test.csv"
        self.train_file_final = "training.csv"
        self.test_file_final = "test.csv"

    def extract_and_rename(self):
        try:
            logger.info("Starting training/test extraction process...")

            # Ensure processed folder exists
            os.makedirs(self.processed_dir, exist_ok=True)

            # Temporary extraction folder
            os.makedirs(self.temp_extract_dir, exist_ok=True)

            if not os.path.exists(self.raw_zip_path):
                raise FileNotFoundError(f"{self.raw_zip_path} not found.")

            # Unzip the dataset
            with zipfile.ZipFile(self.raw_zip_path, 'r') as zip_ref:
                zip_ref.extractall(self.temp_extract_dir)
            logger.info(f"Extracted zip to {self.temp_extract_dir}")

            # Copy and rename train and test files
            src_train_path = os.path.join(self.temp_extract_dir, self.train_file_original)
            src_test_path = os.path.join(self.temp_extract_dir, self.test_file_original)

            dst_train_path = os.path.join(self.processed_dir, self.train_file_final)
            dst_test_path = os.path.join(self.processed_dir, self.test_file_final)

            if not os.path.exists(src_train_path) or not os.path.exists(src_test_path):
                raise FileNotFoundError("Expected CSV files not found in extracted contents.")

            shutil.copy(src_train_path, dst_train_path)
            shutil.copy(src_test_path, dst_test_path)

            logger.info(f"Saved training dataset to {dst_train_path}")
            logger.info(f"Saved test dataset to {dst_test_path}")

            # Clean up temp unzip folder
            shutil.rmtree(self.temp_extract_dir)
            logger.info("Temporary files cleaned up.")

        except Exception as e:
            logger.error("Failed during training/test data preparation.")
            raise CustomException(e, sys)


if __name__ == "__main__":
    splitter = TrainingTestSplit()
    splitter.extract_and_rename()