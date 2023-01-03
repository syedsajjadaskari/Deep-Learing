import os
import urllib.request as request
from zipfile import ZipFile
from deepClassifier.entity import DataIngestionConfig
from deepClassifier import logger
from deepClassifier.utils import get_size
from pathlib import Path

from tqdm import tqdm #shows progress bar

class DataIngestion:
    def __init__(self, config:DataIngestionConfig):
        self.config = config

    def download_file(self):
        logger.info("Trying to download file ....")
        if not os.path.exists(self.config.local_data_file):
            logger.info("Download started")
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(f"{filename} download with following info: \n {headers}")
        else:
            logger.info(f"file already exist:{get_size(Path(self.config.local_data_file))}")
    #Condition to store only cat and dog files
    def _get_updated_list_of_files(self, list_of_files):
        return [f for f in list_of_files if f.endswith(".jpg") and ("cat" in f or "Dog" in f)]
    #preprocessing
    def _preprocessing(self, zf: ZipFile, f: str, working_dir: str):
        target_filepath = os.path.join(working_dir, f)
        #if not present in path then extract
        if not os.path.exists(target_filepath):
            zf.extract(f, working_dir)
        #if dummy stored the remove
        if os.path.getsize(target_filepath)==0:
            logger.info(f"removing file{target_filepath} with size:{get_size(Path(self.config.local_data_file))}")
            os.remove(target_filepath)


    def unzip_and_clean(self):
        logger.info(f"unzip file and removing unwanted files")
        with ZipFile(file = self.config.local_data_file, mode = "r") as zf:
            list_of_files = zf.namelist()
            #store specificed file
            updated_list_of_files = self._get_updated_list_of_files(list_of_files)
            for f in tqdm(updated_list_of_files):
                self._preprocessing(zf, f, self.config.unzip_dir)

