from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from time import sleep
from time import strftime
import logging


class Logger(object):

    def logging_test(self):
        #logger = logging.getLogger('sample_log')
        logger = logging.getLogger(Logger.__name__)
        logger.setLevel(logging.INFO)

        #creating console handler

        handler = logging.StreamHandler()
        handler.setLevel(logging.INFO)
        #creating formatter

        formatter = logging.Formatter('%(asctime)s, %(name)s: %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        handler.setFormatter(formatter)

        logger.addHandler(handler)

        logger.debug("debug")
        logger.info("info")
        logger.error("error")
        logger.warning("warning")

test = Logger()
test.logging_test()

