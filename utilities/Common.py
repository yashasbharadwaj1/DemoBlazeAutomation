import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    def verifyLinkPresence(self, text):
        wait = WebDriverWait(self.driver, 6)
        wait.until(
            expected_conditions.presence_of_element_located((By.LINK_TEXT, text))
        )

    def returnAlertText(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.alert_is_present())
        alert = self.driver.switch_to.alert
        text = alert.text
        return text

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        logger.setLevel(logging.DEBUG)

        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        return logger
