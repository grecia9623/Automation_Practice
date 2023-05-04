import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class miclase_unittest(unittest.TestCase):

    def setUp(self):

        s = Service("C:/chromedriver/chromedriver.exe")
        self.driver= webdriver.Chrome(service=s)
        self.driver.maximize_window()

    def test_clic_en_link_text(self):
        driver = self.driver
        driver.get("https://www.google.com.mx/")
        enlace =driver.find_element(By.LINK_TEXT, "Gmail")
        enlace.click()


    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
