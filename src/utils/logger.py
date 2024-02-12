import logging
from configparser import ConfigParser


class Logger:
    def __init__(self, config_file_path='logger.ini', logger_name='market_logger'):
        self.logger = self.setup_logger(config_file_path, logger_name)

    def setup_logger(self, config_file_path, logger_name):
        config = ConfigParser()
        config.read(config_file_path)

        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.DEBUG)

        file_handler = logging.FileHandler(config.get('log_config', 'file_path'))
        file_handler.setLevel(getattr(logging, config.get('log_config', 'level')))

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

        return logger

    def get_logger(self):
        return self.logger

    def __call__(self, *args, **kwargs):
        return self.get_logger()
