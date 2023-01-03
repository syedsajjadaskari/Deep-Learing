from deepClassifier.config import ConfigurationManager
from deepClassifier.components import DataIngestion

STAGE_NAME = "Data Ingestion stage"

from deepClassifier import logger

def main():
    config = ConfigurationManager()
    data_ingestion_config = config.get_data_ingestion_config()
    data_ingestion = DataIngestion(config = data_ingestion_config)
    data_ingestion.download_file()
    data_ingestion.unzip_and_clean()




if __name__ == '__main__':
    try:
        logger.info(f">>>> stage {STAGE_NAME} started <<<<<")
        main()
        logger.info(f">>>> stage {STAGE_NAME} completed <<<<")
    except Exception as e:
        logger.exception(e)
        raise e