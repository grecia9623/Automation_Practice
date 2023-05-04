import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

class miclase_unittest(unittest.TestCase):

    def setUp(self):

        s= Service("C:/chromedriver/chromedriver.exe")
        self.driver= webdriver.Chrome(service=s)
        self.driver.maximize_window()

    def test_presionar_Enter(self):
        driver = self.driver
        driver.get("https://www.google.com")
        busqueda=driver.find_element(By.NAME, "q")
        busqueda.send_keys("Stranger things metallica scene")
        busqueda.send_keys(Keys.ENTER)
        time.sleep(2)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
