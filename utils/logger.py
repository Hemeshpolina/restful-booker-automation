import logging

def setup_logger():
    logger = logging.getLogger("restful_booker")
    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler("reports/logfile.log")
    fh.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger