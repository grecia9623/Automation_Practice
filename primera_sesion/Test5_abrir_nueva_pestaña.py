import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

class miclase_unittest(unittest.TestCase):

    def setUp(self):
        s = Service("C:/chromedriver/chromedriver.exe")
        self.driver = webdriver.Chrome(service=s)
        self.driver.maximize_window()

    def test_navegar_entre_pestañas(self):
        driver = self.driver
        driver.get("http://www.google.com")
        time.sleep(3)
        driver.execute_script("window.open('');")
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[1])
        driver.get("https://www.python.org")
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(3)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
