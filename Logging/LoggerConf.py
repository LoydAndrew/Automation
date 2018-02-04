from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from time import sleep
from time import strftime
import logging
import logging.config


class LoggerConfig(object):

    def logging_test(self):
        logging.config.fileConfig('logging.conf')
        logger = logging.getLogger(LoggerConfig.__name__) # name of the class



        #console messages

        logger.debug("debug")
        logger.info("info")
        logger.error("error")
        logger.warning("warning")
        logger.critical('critical')


demo = LoggerConfig()
demo.logging_test()