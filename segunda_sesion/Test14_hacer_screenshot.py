import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import *

class usando_unittest(unittest.TestCase):
    def setUp(self):
        s = Service("C:/chromedriver/chromedriver.exe")
        self.driver = webdriver.Chrome(service=s)
        self.driver.maximize_window()

    def test_obtener_screenshot(self):
        driver = self.driver
        driver.get("http://www.google.com")
        try:
            element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "q")))
        except TimeoutException:
            print("-----No se encontro el elemento-----")
        finally:
            driver.save_screenshot("test_obtener screenshot con q.png")


    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
