import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class miclase_unittest(unittest.TestCase):

    def setUp(self):
        s = Service("C:/chromedriver/chromedriver.exe")
        self.driver = webdriver.Chrome(service=s)
        self.driver.maximize_window()

    def test_pagina_anterior(self):
        driver = self.driver
        driver.get("https://www.youtube.com")
        driver.get("https://www.python.org")
        driver.get("https://www.google.com")
        time.sleep(2)
        driver.back()
        time.sleep(2)
        driver.back()
        time.sleep(2)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
